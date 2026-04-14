# PublicRights-Aapkaadhikar-AIbot
AI-powered Telegram bot that generates for civil laws (court-style) notices in PDF format

# PublicRights (Aapkaadhikar)

AI-powered Telegram bot that generates court-style legal notices in PDF format.

## Features
- Lawyer-style legal notice generation
- AI-based query understanding
- Telegram bot integration
- PDF export (court-ready format)

## Tech Stack
- FastAPI
- Python
- ReportLab
- Telegram Bot API

## Setup

### 1. Clone repo
```bash
git clone https://github.com/SarboJ/PublicRights-Aapkaadhikar-_AIbot.git

###  2. Install dependencies
pip install -r requirements.txt

###  3. Add env variables
BOT_TOKEN

###  4. Run server
uvicorn app.main:app --reload

###  5. Webhook
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://your-domain/webhook"

⚠️ Disclaimer

This tool provides AI-generated legal drafts and does not constitute legal advice

cd publicrights-bot
