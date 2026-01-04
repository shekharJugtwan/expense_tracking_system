import logging


#creating a custome logger
def setup_logging(name, log_file = 'server.log', level = logging.DEBUG):
    logger = logging.getLogger(name)

    #configuring the customer logger
    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

