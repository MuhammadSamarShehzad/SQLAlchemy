import logging

# Configure logging
logging.basicConfig(
    filename="app.log",              # log file name
    level=logging.DEBUG,             # log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

# Get a logger instance
logger = logging.getLogger(__name__)
