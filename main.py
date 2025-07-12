from openai import OpenAI
import os
import requests
from dotenv import load_dotenv


try:
    # Load environment variables from .env file
    load_dotenv()

    # OpenRouter client
    client = OpenAI(
        base_url=os.getenv("OPENROUTER_BASE_URL"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

    # Get AI-generated trivia
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528:free",
        messages=[
            {
                "role": "user",
                "content": """
                
                Ignore telegram formatting instructions.
                Give me basic to intermediate grammar tip or rule that is useful for improving my spoken English. Use the following structure and keep the content short and concise: 
                
                Grammar Topic:
                [short title of the grammar point]

                ================
                
                Example & Explanation:  
                [Give 1 or 2 example sentences. Explain briefly how the rule is applied]"""
            }
        ]
    )

    trivia_content = completion.choices[0].message.content

    # Telegram bot info
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    # Send to telegram
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": trivia_content}

    response = requests.post(url, data=payload)
    print("Status:", response.status_code)
    print("Response:", response.text)

    print("✅ Script completed successfully!")

except Exception as e:
    print(f"❌ Script failed: {e}")
