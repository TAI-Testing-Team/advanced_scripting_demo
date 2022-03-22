'''
This script refreshes the browser window.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
	driver=context.get_driver()
	driver.execute_command('RefreshCommand', [])
	context.get_all_elements()