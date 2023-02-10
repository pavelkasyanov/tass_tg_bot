import datetime
import locale
import time

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

WEATHER_TEMPLATE = """
Доброе утро, Питер! ❤️

Погода на {week_day}, {day} {month}:

Утром 0 Пасмурно☁️
Днём −1…0 Пасмурно☁️
Вечером −1…0 Пасмурно☁️
Ночью −2…−1 Дождь со снегом💧❄️
""".format(
    week_day=time.strftime("%A"), day=datetime.date.today().day, month=time.strftime("%B")
)
