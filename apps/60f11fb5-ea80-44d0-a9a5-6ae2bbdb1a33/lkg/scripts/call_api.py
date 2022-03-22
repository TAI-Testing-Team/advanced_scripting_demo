import requests, json
import logging
log = logging.getLogger(__name__)

# This script calls the API and retrieves the App ID (60f11fb5-ea80-44d0-a9a5-6ae2bbdb1a33) and inputs it into the text area box (inp_test_info)

def run(context):
    resp = requests.get("http://localhost:12543/api/v1/dashboard")
    data = resp.json().get("data",[])
    data_into_string = json.dumps(data) #makes JSON object returned in line 9 into string
    context.perform_gesture('text_entry_no_submit','inp_test_info', data_into_string) 

    # log.info('=====================data request======================')
    # log.info(data)
    # log.info('======================json dumps======================')
    # log.info(json_string)