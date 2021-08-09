from random import randint
from json import loads
import aiohttp, logging


async def porfirevich(user_text):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
    }
    json = {
        "prompt": user_text,
        "length": randint(10, 60),
        "num_samples": 1
    }
    url = "https://pelevin.gpt.dobro.ai/generate/"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, json=json) as resp:
                return loads(await resp.text())
    except aiohttp.ClientError as e:
        logging.error("%s: %s" % (porfirevich.__name__, e))