import logging

logger = logging.getLogger()
fhandler = logging.FileHandler(filename='/Users/sikalidas/PycharmProjects/Python_API_Main/Logs/testLogs.txt', mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)