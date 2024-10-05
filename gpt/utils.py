from openai import AsyncOpenAI
from config import Config

client = AsyncOpenAI(
    base_url=Config.OPENAI_URL,
    api_key=Config.OPENAI_KEY
)


def generate_messages(prompt):
    return [
        {
            "role": "system",
            "content": "You are an excellent English assistant"
        },
        {
            "role": "user",
            "content": prompt
        }
    ]


async def process_prompt(prompt: str) -> str | None:
    messages = generate_messages(prompt)
    answer = await client.chat.completions.create(
        model=Config.OPENAI_MODEL,
        messages=messages
    )

    return answer.choices[0].message.content
