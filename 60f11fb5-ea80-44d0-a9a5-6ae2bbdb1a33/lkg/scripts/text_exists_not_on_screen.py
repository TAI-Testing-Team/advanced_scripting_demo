import logging

log = logging.getLogger(__name__)

def run(context):
    text_exists=context.text_exists("Kinetic") #string is on Find Elements page 
    if text_exists==True:
        context.perform_gesture('text_entry_no_submit', 'inp_test_info', 'Text exists on screen')
    else:
        context.perform_gesture('text_entry_no_submit', 'inp_test_info', 'Text does not exist on screen')