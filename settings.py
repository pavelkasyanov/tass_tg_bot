from dotenv import dotenv_values


class AppSettings:
    def __init__(self) -> None:

        config = dotenv_values(".env", verbose=True)

        self.BOT_API_KEY = config.get("BOT_API_KEY")
        self.CHAT_ID = int(config.get("CHAT_ID") or 0)
        self.YANDEX_WEATHER_API_KEY = config.get("YANDEX_WEATHER_API_KEY")
        self.LOCATION_LAT = config.get("LOCATION_LAT")
        self.LOCATION_LON = config.get("LOCATION_LON")


settings = AppSettings()
