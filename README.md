# 📬 SQL Daily Tips Telegram Bot

This Python script generates **SQL Optimization Tips** using an AI model via [OpenRouter](https://openrouter.ai), then sends it as a message to a Telegram chat using the Telegram Bot API.
I automate the script using [https://www.pythonanywhere.com], free account only so I'm only limited to 1 scheduled task per day.

---

## 💡 What It Does

- Connects to an OpenRouter-compatible AI model (`deepseek-r1-0528:free`)  
- Prompts it to return a structured trivia fact (Topic, Fact, Explanation)  
- Sends the result to a Telegram channel or user using your bot token

---

## 🛠️ Requirements

- Python
- Telegram Bot Token
- OpenRouter API Key and Base URL
- Telegram Chat ID (for where the trivia will be sent)
- pythonanywhere account (free) 

---

## 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/ai-trivia-telegram-bot.git
   cd ai-trivia-telegram-bot
