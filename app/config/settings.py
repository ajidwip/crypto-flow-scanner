import os

from app.config.environment import *


def get_env(key: str, default=None):
    value = os.getenv(key)
    return value if value is not None else default


class Settings:

    APP_NAME = get_env("APP_NAME", "Crypto Flow Scanner")

    APP_VERSION = get_env("APP_VERSION", "1.0.0")

    LOG_LEVEL = get_env("LOG_LEVEL", "INFO")

    DATABASE_PATH = get_env("DATABASE_PATH", "storage/database/scanner.db")

    CACHE_PATH = get_env("CACHE_PATH", "storage/cache")

    LOG_PATH = get_env("LOG_PATH", "storage/logs")

    TEMP_PATH = get_env("TEMP_PATH", "storage/temp")

    BINANCE_REST = get_env("BINANCE_REST", "https://fapi.binance.com")

    BINANCE_WS = get_env("BINANCE_WS", "wss://fstream.binance.com/ws")

    SCAN_INTERVAL = int(get_env("SCAN_INTERVAL", 60))

    CONFIRMATION_INTERVAL = int(get_env("CONFIRMATION_INTERVAL", 300))

    OPEN_INTEREST_INTERVAL = int(get_env("OPEN_INTEREST_INTERVAL", 300))

    FUNDING_INTERVAL = int(get_env("FUNDING_INTERVAL", 300))

    SYMBOL_REFRESH_INTERVAL = int(get_env("SYMBOL_REFRESH_INTERVAL", 3600))


settings = Settings()