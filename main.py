from fastapi import FastAPI, Request
import requests
import os

from agent.py import extract_notice_fields
from pdfbuilt.py import generate_legal_notice

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.get("/")
def home():
    return {"status": "PublicRights Bot Running"}

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        # Extract structured fields
        structured = extract_notice_fields(text)

        # Generate PDF
        pdf_path = generate_legal_notice(structured)

        # Send PDF
        url = f"{TELEGRAM_API}/sendDocument"
        with open(pdf_path, "rb") as pdf:
            requests.post(url, data={"chat_id": chat_id}, files={"document": pdf})

    return {"status": "ok"}
