import logging

log = logging.getLogger(__name__)

# This script enters text into the input field. It is an embedded script in a subfolder of scripts folder so it is called using a script that is in the scripts folder.

def run(context):
    context.perform_gesture('text_entry_no_submit', 'inp_test_info', 'Made changes from myscript_organized.py')

