import logging

# logging.debug('This is a debug message')
# logging.info('This is an Info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')

# Loggin to file

# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug

# numeric_level = getattr(logging, loglevel.upper(), None)
# if not isinstance(numeric_level, int):
#     raise ValueError('Invalid log level: %s' % loglevel)
# logging.basicConfig(level=numeric_level)
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

