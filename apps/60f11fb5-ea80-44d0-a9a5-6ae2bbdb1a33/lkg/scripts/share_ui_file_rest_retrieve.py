import logging
# from csv import DictReader
import json


log = logging.getLogger(__name__)

def run(context):

    # access the internal test case datastore (part of the `context` object)
    script_vals = context.get_test_script_vals()

    # retrieve stored data from the previous test steps
    stored_api_data = script_vals.get('api_data')
    stored_csv_data = script_vals.get('csv_data')
    stored_btn_text = script_vals.get('btn_info')
    
#turn api data into a string
    api_data_json_string = json.dumps(stored_api_data) 
    # This data is now available for use in this step:

    # assertions:
    assert stored_csv_data[0].get('my_label') == 'inp_email', 'Data from this step does not match imported data'
    # refresh page by clicking on Dynamic menu item
    context.perform_gesture('tap', 'lnk_dynamic')

    # item = csv_data[0].get('my_label')
    # actions:
    context.perform_gesture('text_entry_no_submit', 'inp_test_info', stored_btn_text)
    context.verify(grep=stored_btn_text)
    context.perform_gesture('tap', 'lnk_dynamic')
    context.perform_gesture('text_entry_no_submit', 'inp_test_info', api_data_json_string)
    context.verify(grep=api_data_json_string)
    context.perform_gesture('tap', 'lnk_dynamic')
    context.perform_gesture('text_entry_no_submit', 'inp_test_info', 'Successfully called stored csv_file, stored api data, and stored button text name.')


    
    # TROUBLESHOOTING CODE

    # External data storage:
    # requests.post('http://localhost:8000/api/test', json={'screen_text': btn_change_text})

    # log.info('====================output ====================')
    # log.info('success!')
    # log.info('====================end ====================')