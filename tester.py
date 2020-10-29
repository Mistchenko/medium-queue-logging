import logging
from datetime import datetime


# logger = logging.getLogger(__name__)
logger = logging.getLogger('tester')


def test_run():
    t1 = datetime.today()
    a = ''.join(['.' for a in range(100000000)])
    print('Data generator:\t', t1, '\t', datetime.today() - t1)

    t1 = datetime.today()
    logger.critical(a)
    print('Log push:\t', t1, '\t', datetime.today() - t1)

    logger.warning('Test complete')
