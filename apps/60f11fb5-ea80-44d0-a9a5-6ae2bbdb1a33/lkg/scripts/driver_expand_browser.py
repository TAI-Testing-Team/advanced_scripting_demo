'''
This script opens the browser with a custom height and width to a specified url.
Use the format https://url to replace <your URL> below.
This example uses the current height but increases the width by 1.5 * the current width, modify as needed.
'''

import logging
import time

log = logging.getLogger(__name__)

def run(context):
	driver=context.get_driver()
	driver.execute_command('ResizeCommand', [1920, 1080])