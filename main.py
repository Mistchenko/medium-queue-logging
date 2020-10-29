import os
import logging
import logging.config
import yaml
from tester import test_run
from datetime import datetime


with open('_error.log', 'w') as f:
    f.write('')

# with open('conf.yaml', 'r') as f:
with open('conf_base.yaml', 'r') as f:
    logconfig_dict = yaml.load(f.read(), Loader=yaml.FullLoader)

logging.config.dictConfig(logconfig_dict)
main_logger = logging.getLogger('app')

t1 = datetime.today()
test_run()
main_logger.info('Stop')
print('App time:\t', t1, '\t', datetime.today()-t1)
