import logging
import requests
from csv import DictReader
import json

log = logging.getLogger(__name__)

def run(context):

# 1: query API

    # use Requests module to perform API CRUD operations (GET/POST/PUT/DELETE/etc...)
    # and capture the response
    resp = requests.get('http://localhost:12543/api/v1/dashboard')
    api_data = resp.json().get("data",[])
# 2: access context datastore and add data for use in subsequent test steps:
    # access the internal test case datastore (part of the `context` object)
    script_vals = context.get_test_script_vals()
    # add captured data to the TC datastore for use in subsequent steps
    script_vals['api_data'] = api_data
    json_string = json.dumps(api_data) 
    context.perform_gesture('tap', 'lnk_dynamic')
    context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    log.info('=====================data request======================')
    log.info(api_data)
    log.info('======================json dumps======================')
    log.info(json_string)