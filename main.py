import sys
import logging
import json
from pathlib import Path

from app import launch_app

CONFIG_PATH = Path("config/config.json")
LOG_PATH = Path("logs/app.log")

def setup_logging():
    LOG_PATH.parent.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.info("Logging initialized")

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    else:
        logging.info("No config file found")
        return {}

def main():
    setup_logging()
    config = load_config()
    logging.info("Config loaded")
    launch_app(config)

if __name__ == "__main__":
    main()