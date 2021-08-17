from aiogram import executor
from dispatcher import dp
import handlers, logging

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)