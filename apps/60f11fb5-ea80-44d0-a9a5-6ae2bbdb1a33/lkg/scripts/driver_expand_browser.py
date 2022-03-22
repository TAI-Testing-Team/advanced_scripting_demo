'''
This script opens the browser with a custom height and width to a specified url.

'''

import logging
import time

log = logging.getLogger(__name__)

def run(context):
	driver=context.get_driver()
	driver.execute_command('ResizeCommand', [1920, 1080])
	context.get_all_elements()