import requests, json
import logging
log = logging.getLogger(__name__)

def run(context):

     # access the internal test case datastore (part of the `context` object)
    script_vals = context.get_test_script_vals()
    # add captured data to the TC datastore for use in subsequent steps
    api_data = script_vals['api_data']
    context.perform_gesture('text_entry_no_submit','inp_test_info', api_data) 
