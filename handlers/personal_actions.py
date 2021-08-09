from aiogram import types
from dispatcher import dp
from ..utils import porfirevich
from ..dispatcher import bot


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_chat_action(msg.from_user.id, 'typing')
    add_ = await porfirevich(msg.text)
    await msg.reply("<i>%s</i><b>%s</b>" % (msg.text, add_))