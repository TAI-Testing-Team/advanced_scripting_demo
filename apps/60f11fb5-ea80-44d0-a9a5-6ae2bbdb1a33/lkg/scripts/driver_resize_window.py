'''
This script resizes the browser window to a size you specify.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
	driver=context.get_driver()
	driver.execute_command('ResizeCommand', [200, 300])