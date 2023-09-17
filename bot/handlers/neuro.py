from json import loads
from aiohttp import ClientSession


async def process_prompt(prompt: str) -> str | None:
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are an English assistant"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": True
    }

    answer = ""

    try:
        async with ClientSession() as session:
            async with session.post(
                    url='http://127.0.0.1:1337/v1/chat/completions',
                    json=data
            ) as r:

                async for line in r.content:
                    string_line = line.decode('utf8').replace("\n", "").removeprefix("data: ")

                    if string_line != "" and string_line != " " and string_line != "\n":
                        result = loads(string_line)

                        choice = result.get("choices")[0].get("delta").get("content")

                        if choice is not None and choice != "" and choice != " ":
                            answer += choice

        return answer

    except:
        return None
