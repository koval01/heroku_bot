from random import randint
from telegraph import Telegraph
from json import loads
import aiohttp, logging, re


async def porfirevich(user_text: str) -> str:
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
            async with session.post(url, headers=headers, json=json) as resp:
                return loads(await resp.text())["replies"][0]
    except aiohttp.ClientError as e:
        logging.error("%s: %s" % (porfirevich.__name__, e))


def striphtml(data: str) -> str:
    p = re.compile(r'<.*?>')
    return p.sub('', data)


async def telegraph_create(text: str) -> str:
    text = striphtml(text)

    telegraph = Telegraph()
    telegraph.create_account(short_name='dark_fantasy0_bot')

    title_text = text

    if len(title_text) > 16:
        title_text = title_text[:13] + "..."

    response = telegraph.create_page(
        title_text,
        html_content=text,
        author_name="@dark_fantasy0_bot",
        author_url="https://t.me/dark_fantasy0_bot",
    )
    return 'https://telegra.ph/' + response['path']


async def create_inline_buttons(*button) -> str:
    array_button = []
    global_array_buttons = []

    for i in button:
        array_button = []
        array_button.append(i)
        global_array_buttons.append(array_button)

    result = dict(inline_keyboard=global_array_buttons)

    return result