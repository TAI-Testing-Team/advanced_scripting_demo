
import logging
import requests

log = logging.getLogger(__name__)

def run(context):

    # get text values from a pricing table. 
    # use `dynamic=True` to allow capture of an element where the text might change,
    # as with shopping cart totals, new user IDs, etc...
    btn_text = context.find_element('btn_change', dynamic=True).get('text')


    log.info('====================output find element====================')
    log.info(btn_text)
    log.info('====================end find element====================')
    
    script_vals = context.get_test_script_vals()

    # add element data for use in subsequent steps
    script_vals['btn_info'] = btn_text

    #refresh page
    context.perform_gesture('tap', 'lnk_dynamic')
    context.perform_gesture('text_entry_no_submit','inp_test_info', script_vals['btn_info']) 
    