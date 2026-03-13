# src/repochat/utils/logger.py

import logging
from rich.logging import RichHandler

# Configure rich logging (colorful output) at INFO level.
logging.basicConfig(
    level=logging.INFO, 
    format="%(message)s", 
    handlers=[RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger("repochat")
