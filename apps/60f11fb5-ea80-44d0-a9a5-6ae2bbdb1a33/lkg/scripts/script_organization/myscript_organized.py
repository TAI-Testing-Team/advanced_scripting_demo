import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('text_entry_no_submit', 'inp_test_info', 'Made changes from myscript_organized.py')

