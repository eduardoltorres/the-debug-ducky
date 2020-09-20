import logging

# Create logger
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

# Create console handler with debug level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#Create file handler which logs even debug messages
fh = logging.FileHandler("ducky.log", mode="w")
fh.setLevel(logging.DEBUG)

#Create formatter and add to handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#Add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)
