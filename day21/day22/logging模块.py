import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='logger.log',
#     filemode='w',
#     format='%(asctime)s,%(lineno)d %(message)s %(filename)s'
#     )#调级别
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

logger=logging.getLogger()
fh=logging.FileHandler('test_log')
ch=logging.StreamHandler()
fm=logging.Formatter('%(asctime)s %(message)s')
fh.setFormatter(fm)
ch.setFormatter(fm)
logger.addHandler(fh)
logger.addHandler(ch)
#--------------------------------
logger.setLevel('DEBUG')
logger.debug('hello')
logger.info('lll aa')
logger.warning('hello aa')
logger.error('hello aa')
logger.critical('aa hello')


