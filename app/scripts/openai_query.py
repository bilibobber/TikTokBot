from dotenv import load_dotenv
import os

from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=os.getenv("OPENAI_BASE_URL"), )


def gpt_answer(promt):
    chat_result = client.chat.completions.create(
        messages=[{"role": "user", "content": promt + '. Напиши кратко, на русском.'}],
        model="deepseek-r1",
        max_tokens=1000,
    )

    return chat_result.choices[0].message.content.strip()
