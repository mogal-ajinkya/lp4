import logging
import time

# Initial logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='basic_logger.log',
    filemode='w'
)

# Create a custom logger with a specific level
LogWithLevelName = logging.getLogger('myLoggerSample')
level = logging.getLevelName('INFO')
LogWithLevelName.setLevel(level)

# Infinite loop for continuous logging
while True:
    logging.debug("Debug message")
    logging.info("Informative message")
    logging.error("Error message")
    LogWithLevelName.info("Custom logger message")

    # Delay to avoid overwhelming the log file
    time.sleep(5)  # Logs messages every 5 seconds
