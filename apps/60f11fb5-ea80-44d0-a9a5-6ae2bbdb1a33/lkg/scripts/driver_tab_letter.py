'''
This script sends the tab key command to tab to the next field in a web browser.
It relies on the tab ordering of the web page.
'''

import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    i = 1
    while i < 3:   
    #Executes Tab button
        driver.session.execute_command('SendKeysCommand', [u'\ue004'])
        i+= 1
    # Types letter Z
    driver.session.execute_command('SendKeysCommand', ['\u005A'])
    
    #Executes Tab button
    driver.session.execute_command('SendKeysCommand', [u'\ue004'])


    context.get_all_elements()