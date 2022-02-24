import logging

log = logging.getLogger(__name__)

def run(context):
    element_exists=context.element_exists('btn_change', dynamic=False)
    if element_exists==True:
        context.perform_gesture('text_entry_no_submit', 'inp_test_info', 'Element exists on screen')
    else:
        context.perform_gesture('text_entry_no_submit', 'inp_test_info', 'Element does not exist')
