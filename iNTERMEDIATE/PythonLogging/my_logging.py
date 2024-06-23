import logging
import os


def setup_custom_logger(name):
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ##### Create handlers #####
    # Creates a console handler (StreamHandler) that outputs log messages to the console.
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG)

    # Creates a file handler (FileHandler) that outputs log messages to a file named app.log.
    f_handler = logging.FileHandler('app.log')
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


def main():
    logger = setup_custom_logger('Fatlindi')

    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

    try:
        x = 1 / 0
    except ZeroDivisionError:
        logger.exception("An exception occurred")


if __name__ == "__main__":
    main()
