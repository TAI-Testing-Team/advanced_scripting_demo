import logging
import json
log = logging.getLogger(__name__)

# This script finds all of the elements with THAT label on the page and collects them.  
# Like context.find_element, it returns the Element Info for all of these elements
# Since it had the dynamic flag, it will return all the info on these elements, even if they are 'dynamic'.

def run(context):
    matched_elements = context.find_elements_with_label('btn_blue', dynamic=False)
    json_string = json.dumps(matched_elements) #makes JSON object returned in line 9 into string
    context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    context.verify(grep=json_string)
    #inputs string into Text Area input 