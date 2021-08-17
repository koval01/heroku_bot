import logging, asyncio

from aiogram import types
from dispatcher import dp
from utils import porfirevich, telegraph_create, create_inline_buttons
from telegraph.exceptions import TelegraphException
from dispatcher import bot


async def send_(msg: object) -> None:
    logging.info("Message by (%d)" % msg.chat.id)
    me = await bot.get_me()

    while True:
        try:
            group_name = None

            if msg.chat.type != "private":
                me = "@"+me["username"]
                if me not in msg.text:break

            await bot.send_chat_action(msg.chat.id, 'typing')

            add_ = await porfirevich(msg.text)
            data_ = add_["json_"]

            if msg.chat.type != "private":
                data_ = data_[0:1]
                group_name = msg.chat.title

            for i in data_:
                msg.text = msg.text.replace(me, "")
                text_ = "<i>%s</i><b>%s</b>" % (msg.text, i)

                if group_name:
                    text_ph = "<i>%s</i><b>%s</b> | <b>Сгенерировано участником группы «%s» - «%s»</b>" \
                              % (msg.text, i, group_name, msg.from_user.full_name)

                else:
                    text_ph = text_

                telegraph_ = await telegraph_create(text_ph)

                link = await create_inline_buttons(
                    {"text": "Telegra.ph", "url": telegraph_}
                )

                await msg.reply(text_, reply_markup=link)

        except TelegraphException as e:
            logging.debug(e)
            await asyncio.sleep(5)  # sleep five seconds

        except Exception as e:
            await msg.reply(
                "Traceback: <code>%s</code>" % e,
            )

            if msg.chat.type != "private": break

        else:
            break


@dp.message_handler(commands="start")
async def cmd_ping_bot(msg: types.Message):
    msg.text = "Лера любила гулять"
    await send_(msg)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await send_(msg)
