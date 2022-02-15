import requests, json
import logging
log = logging.getLogger(__name__)

def run(context):
    resp = requests.get("http://localhost:12543/api/v1/dashboard")
    data = resp.json().get("data",[])
    json_string = json.dumps(data) #makes JSON object returned in line 9 into string
    context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    log.info('=====================data request======================')
    log.info(data)
    log.info('======================json dumps======================')
    log.info(json_string)