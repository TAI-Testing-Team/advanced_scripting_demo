'''
This script refreshes the browser window. You may need to add a wait before get_all_elements if page takes time to load after the refresh.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
	driver=context.get_driver()
	driver.execute_command('RefreshCommand', [])
	context.get_all_elements()