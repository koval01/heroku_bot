from random import randint
from json import loads
import aiohttp


async def porfirevich(user_text):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://pelevin.gpt.dobro.ai/generate/", json={
            "prompt": user_text,
            "length": randint(10, 60),
            "num_samples": 1,
        }) as response:
            return loads(await response.text())["replies"][0]