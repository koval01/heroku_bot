from aiogram import types
from dispatcher import dp
from utils import porfirevich, telegraph_create, create_inline_buttons
from dispatcher import bot


async def send_(msg: object) -> None:
    try:
        await bot.send_chat_action(msg.from_user.id, 'typing')
        add_ = await porfirevich(msg.text)
        data_ = add_["json_"]
        
        for i in data_:
            text_ = "<i>%s</i><b>%s</b>" % (msg.text, i)
            telegraph_ = await telegraph_create(text_)

            link = await create_inline_buttons(
                {"text": "Telegra.ph", "url": telegraph_}
            )

            await msg.reply(text_, reply_markup=link)
        
    except Exception as e:
        await msg.reply("Traceback: %s\n\nServer Response: %s" % (e, add_["server_resp"]))


@dp.message_handler(commands="start")
async def cmd_ping_bot(msg: types.Message):
    msg.text = "Феминизм это"
    await send_(msg)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await send_(msg)
