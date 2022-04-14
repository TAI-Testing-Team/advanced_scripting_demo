'''
This script opens the browser with a custom height and width to a specified url.
Use the format https://url to replace <your URL> below.
This example uses the current height but increases the width by 1.5 * the current width, modify as needed.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    d = driver.get_window_size()
    width = d['width']
    height = d['height']
    new_width = int(1.5 * float(width))
    new_height = height
    driver.set_window_size(new_width, new_height)
    driver.get('http://blogen-inc.surge.sh/dynamic.html')
    context.get_all_elements()	