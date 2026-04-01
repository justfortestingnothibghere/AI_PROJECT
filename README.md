# ⟡ AI_PROJECT — Powered By t.me/TEAM_X_OG

A lightweight and high-performance AI API built with Python and the Groq LLM platform.
This project exposes a minimal HTTP endpoint to interact with an AI model and receive fast responses.

The API is designed for simplicity, scalability and fast deployment on VPS or cloud platforms.

---

## ⟡ API Endpoint

/?teamdev={query}

Example:
```url
/?teamdev=Hello
```

Example Response:
```bash
{
  "query": "Hello",
  "response": "Hello! How can I assist you today?"
}
```
---

## ⟡ Features

_▸ Minimal API architecture
▸ Groq LLM integration
▸ Multiple API key rotation
▸ JSON formatted responses
▸ Lightweight dependencies
▸ VPS & cloud deployment ready
▸ Docker container support_

---

## ⟡ Model Configuration

_Model used:_
# llama-3.3-70b-versatile

---

## ⟡ Project Structure
```shell
AI_PROJECT
│
├── api.py
├── requirements.txt
├── Dockerfile
└── README.md
```
---

# ⟡ Installation

# Clone repository:
```bash
git clone https://github.com/justfortestingnothibghere/AI_PROJECT.git
cd AI_PROJECT
```

## Install dependencies:
```bash
pip install -r requirements.txt
```
## Run API:
```bash
python api.py
```
---

## ⟡ Docker Support
```Dockerfile
Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "api.py"]
```
---

# Running With Docker

## Build image:
```bash
docker build -t ai_project .
```
## Run container:
```bash
docker run -d -p 5000:5000 ai_project
```
# API will be available at:
```url
http://SERVER_IP:5000/?teamdev=hello
```
---

# ⟡ Deployment Guide

## ▣ Render Deployment

1. Push project to GitHub | Fork This Repository
2. Open Render Dashboard
3. Create New Web Service
4. Connect GitHub repository
5. Configure settings

## Build Command:
```bash
pip install -r requirements.txt
```
## Start Command:
```bash
python api.py
```
_Render will generate a public URL automatically._

## Example:
```url
https://your-app.onrender.com/?teamdev=hello
```
---

# ▣ VPS Deployment

## Update server:
```bash
sudo apt update
```
## Install dependencies:
```bash
sudo apt install python3-pip git -y
```
## Clone repository:
```bash
git clone https://github.com/justfortestingnothibghere/AI_PROJECT.git
cd AI_PROJECT
```
## Install requirements:
```bash
pip install -r requirements.txt
```
## Run API:
```bash
python api.py
```
## Production run (recommended):
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 api:app
```
---

## ⟡ Developer

## _Dev_  : @MR_ARMAN_08 | t.me/MR_ARMAN_08

## ⟡ Support

## _Support_ : @TEAM_X_OG | t.me/TEAM_X_OG

---

## ⟡ License

This project is provided for educational and experimental purposes. for dull read LICENCE file
