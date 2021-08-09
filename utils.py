from random import randint
import aiohttp


async def porfirevich(user_text):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://pelevin.gpt.dobro.ai/generate/', json={
            "prompt": user_text,
            "length": randint(10, 60),
            "num_samples": 1,
        }) as resp:
            return await resp.json()["replies"][0]