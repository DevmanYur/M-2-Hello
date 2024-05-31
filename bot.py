import os
from datetime import datetime

import requests
import telegram
from dotenv import load_dotenv
import logging
import time
import random

from lists import yriy_list_good, yriy_list_trigger

logger = logging.getLogger('Logger')


class TelegramLogsHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def get_notification(tg_bot, chat_id):
    while True:
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            time.sleep(1)
            if current_time == '08:30':
                yriy_list_good_random = random.choice(yriy_list_good)
                yriy_list_trigger_random = random.choice(yriy_list_trigger)
                text = (f'Доброе утро! \n'
                        f'\n'
                        f'Юрию \n'
                        f'  нравится {yriy_list_good_random}\n'
                        f'  не нравится {yriy_list_trigger_random}\n')
                tg_bot.send_message(chat_id=chat_id, text=text)
                time.sleep(36000)
        except requests.exceptions.ReadTimeout:
            logger.info("Истекло время тайм-аута")
            continue
        except requests.exceptions.ConnectionError:
            logger.info("Нет соединения с интернетом")
            time.sleep(1)
            continue
        except :
            logger.info("---")
            time.sleep(1)
            continue


def main():
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']

    tg_bot = telegram.Bot(token=telegram_token)
    chat_id = tg_bot.get_updates()[0].message.from_user.id

    logger.setLevel(logging.DEBUG)
    logger.addHandler(TelegramLogsHandler(tg_bot, chat_id))

    get_notification( tg_bot, chat_id)


if __name__ == '__main__':
    main()
