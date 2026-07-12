import logging

from pathlib import Path

from colorlog import ColoredFormatter

LOG_FOLDER = Path("storage/logs")

LOG_FOLDER.mkdir(parents=True, exist_ok=True)

formatter = ColoredFormatter(

    "%(log_color)s%(asctime)s | %(levelname)s | %(message)s",

    datefmt="%H:%M:%S",

)

logger = logging.getLogger("FLOW")

logger.setLevel(logging.INFO)

stream = logging.StreamHandler()

stream.setFormatter(formatter)

logger.addHandler(stream)