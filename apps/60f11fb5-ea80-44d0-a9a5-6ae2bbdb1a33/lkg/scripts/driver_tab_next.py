'''
This script sends the tab key command to tab to the next field in a web browser.
It relies on the tab ordering of the web page.
'''

import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    context.get_driver().session.execute_command('SendKeysCommand', [u'\ue004'])
    context.get_all_elements()