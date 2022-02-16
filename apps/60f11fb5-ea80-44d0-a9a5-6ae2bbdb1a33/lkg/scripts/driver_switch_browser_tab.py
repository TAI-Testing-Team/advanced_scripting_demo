'''
This script puts focus on a specific named browser tab.
Useful for verification of links that open in a new browser tab by default.
Replace <your tab title> below.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("Blogen - Social Network")
    context.get_all_elements()