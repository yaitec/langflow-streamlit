from langflow_streamlit.utils import default
from rich.console import Console
from rich.logging import RichHandler
import logging
import sys

LOGGER = logging.getLogger("langflow-streamlit")

console = Console()
handler = RichHandler(console=console)
handler.setLevel(logging.DEBUG)

LOGGER.addHandler(handler)

log_levels = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG
}

def generate_log():
   LOGGER.setLevel(logging.DEBUG)
   LOGGER.addHandler(logging.FileHandler('langflow-streamlit.log'))

def logger_set_level(level: str):
    if isinstance(level, int):
        LOGGER.setLevel(level)
    elif level in log_levels:
        LOGGER.setLevel(log_levels[level])
    else:
        raise Exception(f"Invalid log level was provided: {level} must be one of {list(log_levels.keys())}")
