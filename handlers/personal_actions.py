from aiogram import types
from dispatcher import dp
from ..utils import porfirevich


@dp.message_handler()
async def echo_message(msg: types.Message):
    add_ = await porfirevich(msg.text)
    await msg.reply("<i>%s</i><b>%s</b>" % (msg.text, add_))