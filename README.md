# 🤖 AI Gmail Client

An intelligent Python-powered Gmail interface that fetches your latest emails, extracts rich HTML content, and renders them in a browser with beautifully styled formatting — built with AI-readiness in mind.

---

## 🚀 Overview

**AI Gmail Client** is more than just a Gmail reader. It's your stepping stone to building intelligent, automated, and personalized email experiences using Google’s Gmail API + the power of AI.

This client securely authenticates with OAuth 2.0, fetches recent messages, and parses the actual content (including HTML formatting). It sets the stage for advanced features like smart summarization, tagging, prioritization, and AI-powered triage.

---

## ✨ Features

| Feature                         | Description |
|----------------------------------|-------------|
| 🔐 **OAuth 2.0 Secure Login**     | Authenticates via your Google account using a fixed `localhost:8080` port. |
| 📩 **Fetches Latest Emails**     | Retrieves and decodes your most recent Gmail messages. |
| 🧠 **AI-Smart Parsing Engine**   | Recursively extracts the real HTML body, skipping over nested MIME parts. |
| 🌐 **Clean Browser UI**          | Generates a styled `index.html` file showing email previews. |
| 🧠 **AI-Ready Architecture**     | Add AI modules for summarization, spam detection, semantic tagging, and more. |

---

## 💡 AI Enhancement Ideas

Take your email client to the next level by adding any of these features using OpenAI, LangChain, or local LLMs:

- ✉️ **Smart Summarization** — Generate TL;DRs using GPT-4 or LLaMA for long emails.
- 🧹 **Spam Filtering** — Use AI models to flag or hide promotional emails.
- 🔍 **Semantic Search** — Search emails based on meaning, not keywords.
- 🗂 **Topic Classification** — Auto-label emails into categories like "Finance", "Work", or "Urgent".
- 🗣 **Voice Interface** — Add a speech-to-text front end for voice-controlled inbox browsing.
- 📅 **Auto-Action Detection** — Let AI identify meeting invites, bills, or tasks and suggest calendar entries or follow-ups.

---

## 📦 Requirements

- Python 3.6+
- Gmail API enabled in your Google Cloud project
- OAuth 2.0 credentials file

Install dependencies:

```bash
pip install google-auth google-auth-oauthlib google-api-python-client
