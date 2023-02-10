import logging
import threading
import time
from typing import Any, List

import telebot

from settings import settings

from .weather_template import WEATHER_TEMPLATE

YANDEX_LOGO = "По данным Яндекс Погоды."


bot = telebot.TeleBot(settings.BOT_API_KEY)
telebot.logger.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)


def get_weather_message() -> str:
    return WEATHER_TEMPLATE


@bot.message_handler(regexp="/help")
def get_text_message(message: Any) -> None:
    bot.send_message(message.chat.id, "Привет! По всем вопросам обращаться к https://t.me/iPahska")


@bot.message_handler(regexp="/wt")
def get_weather_data(message: Any) -> None:
    bot.send_message(message.chat.id, get_weather_message(), parse_mode="html")


def thread_function() -> None:
    logging.info("Thread starting")
    # bot.send_message(int(config["CHAT_ID"]), "Тестовое сообщение")
    time.sleep(2)
    logging.info("Thread finishing")


def main(argv: List[str]) -> None:
    x = threading.Thread(target=thread_function, args=())
    x.start()
    bot.polling(none_stop=True, interval=0)
    pass


if __name__ == "__main__":
    import sys

    main(sys.argv)
