import logging
import requests
import json

log = logging.getLogger(__name__)

def run(context):

# 1 - Query the API

    # use Requests module to perform API CRUD operations (GET/POST/PUT/DELETE/etc...)
    # and capture the response
    resp = requests.get('http://localhost:12543/api/v1/dashboard')
    data_from_api = resp.json().get("data",[])

# 2 - Access context datastore and add data for use in subsequent test steps

    # access the internal test case datastore (part of the `context` object)
    script_vals = context.get_test_script_vals()
    # add captured data to the TC datastore for use in subsequent steps
    script_vals['api_data'] = data_from_api
    api_data_string = json.dumps(data_from_api) 
    context.perform_gesture('tap', 'lnk_dynamic')
    context.perform_gesture('text_entry_no_submit','inp_test_info', api_data_string)
    context.verify(grep=api_data_string)






    # TROUBLESHOOTING CODE

    # log.info('=====================data request======================')
    # log.info(api_data)
    # log.info('======================json dumps======================')
    # log.info(json_string)