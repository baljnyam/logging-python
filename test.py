import logging

# logging.debug('This is a debug message')
# logging.info('This is an Info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

fdas