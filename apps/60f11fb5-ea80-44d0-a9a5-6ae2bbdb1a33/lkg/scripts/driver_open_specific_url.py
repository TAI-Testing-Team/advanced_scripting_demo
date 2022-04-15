'''
This script opens a specified url in the current browser window.
Use the format https://url to replace <your URL> below.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.get('http://blogen-inc.surge.sh/dynamic.html')
    context.get_all_elements()