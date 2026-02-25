import logging
import os


LOG_DIR = "logs"
LOG_FILE = "trading_bot.log"


def setup_logging():
    # Create logs directory if not exists
    os.makedirs(LOG_DIR, exist_ok=True)

    log_path = os.path.join(LOG_DIR, LOG_FILE)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ],
    )
