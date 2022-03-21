import logging
import json

log = logging.getLogger(__name__)


def run(context):
    labels =['btn_change', 'btn_next', 'btn_confirm'] 
    matched_elements = context.find_elements_with_labels(labels)
    json_string = json.dumps(matched_elements) #makes JSON object returned in line 9 into string
    #inputs string into Text Area input 
    context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 


