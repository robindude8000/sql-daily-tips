from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    api_key=os.getenv("OPENROUTER_API_KEY")
)

completion = client.chat.completions.create(
    model="deepseek/deepseek-r1-0528:free",
    messages=[
        {
          "role": "user",
          "content": "Give me a short random trivia. Summarize it using non-technical words but with simple to intermediate vocabulary"
        }
    ]
)

trivia_content = completion.choices[0].message.content

print(trivia_content)

