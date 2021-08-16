from aiogram import types
from dispatcher import dp
from utils import porfirevich, telegraph_create, create_inline_buttons
from dispatcher import bot


async def send_(msg: object) -> None:
    try:
        await bot.send_chat_action(msg.from_user.id, 'typing')
        add_ = await porfirevich(msg.text)

        text_ = "<i>%s</i><b>%s</b>" % (msg.text, add_)
        telegraph_ = await telegraph_create(text_)
        link = await create_inline_buttons(
            {"text": "Telegra.ph", "url": telegraph_}
        )

        await msg.reply(text_, reply_markup=link)
        
    except Exception as e:
        await msg.reply(e)


@dp.message_handler(commands="start")
async def cmd_ping_bot(msg: types.Message):
    msg.text = "Феминизм это"
    await send_(msg)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await send_(msg)
