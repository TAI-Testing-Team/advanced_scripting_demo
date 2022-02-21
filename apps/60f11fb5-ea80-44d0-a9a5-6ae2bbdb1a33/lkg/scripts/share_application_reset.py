
import logging
import requests

log = logging.getLogger(__name__)

def run(context):

# 1: capture data from the current screen:

    # get text values from a pricing table. 
    # use `dynamic=True` to allow capture of an element where the text might change,
    # as with shopping cart totals, new user IDs, etc...
    btn_text = context.find_element('btn_next', dynamic=True).get('text')

# 2: access context datastore and add data for use in subsequent test steps:
    # access the internal test case datastore (part of the `context` object)
        # write out the text to the log to make sure value stored is correct if needed.
    log.info('====================output find element====================')
    log.info(btn_text)
    log.info('====================end find element====================')
    
    script_vals = context.get_test_script_vals()

    # add element data to the TC datastore for use in subsequent steps
    script_vals['btn_change_info'] = btn_text
    context.perform_gesture('tap', 'lnk_dynamic')
    context.perform_gesture('text_entry_no_submit','inp_test_info', btn_text) 
    