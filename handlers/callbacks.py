from aiogram import types
from dispatcher import dp


@dp.message_handler()
async def echo_message(msg: types.Message):
    await msg.reply("Hello!")

