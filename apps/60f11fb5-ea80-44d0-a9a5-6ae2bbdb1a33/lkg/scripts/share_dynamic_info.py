'''
This script will find the features of an element that has a different string in it each time the bot sees it.
The string (text) value is stored for use later in the test.
The string can alternatively be stored for use in another test by uncommenting the appropriate line at the end of the script.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    # find the properties for the labeled element.
    # dynamic=True devalues text as a model feature so bot will find element even if the text in it changes.
    # request_number can be left as is or changed to whatever you want to call the variable.
    request_number = context.find_element('btn_change', dynamic=True)
    
    # put the text property into a variable that can be used.
    # request_number_text can be left as is or changed.
    # if request_number_text is changed, make sure to change all examples of it in lines below.
    request_number_text = request_number.get('text')
    
    # write out the text to the log to make sure value stored is correct if needed.
    log.info('====================output find element====================')
    log.info(request_number_text)
    log.info('====================end find element====================')
    
    # store the text for use later in the same test
    # request_number_1 can be left as is or changed
    script_vals = context.get_test_script_vals()
    script_vals['request_number_1'] = request_number_text
