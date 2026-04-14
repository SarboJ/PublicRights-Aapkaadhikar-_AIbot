from fastapi import FastAPI, Request
import requests
import os

from app.agent import extract_notice_fields
from app.pdfbuilt import generate_legal_notice

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.get("/")
laws = structured.get("laws", {})

def format_sections(title, items):
    if not items:
        return ""
    return f"\n*{title}:*\n" + "\n".join([f"• {i}" for i in items])

message = "⚖️ *Applicable Legal Provisions:*\n"

message += format_sections("IPC", laws.get("ipc"))
message += format_sections("CrPC", laws.get("crpc"))
message += format_sections("CPC", laws.get("cpc"))
message += format_sections("Consumer Law", laws.get("consumer"))

if message.strip() == "⚖️ *Applicable Legal Provisions:*":
    message += "\nNo direct sections identified."

requests.post(f"{TELEGRAM_API}/sendMessage", json={
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "Markdown"
})
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
