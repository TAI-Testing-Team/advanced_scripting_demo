'''
This script uses a variable set by another script in a different test that created an account. 
This script uses the generated email variable to log in with the unique newly created account. 
'''

import logging
import os
import time
from datetime import datetime

log = logging.getLogger(__name__)

def run(context):
	context.perform_gesture('text_entry_no_submit', 'inp_email', grep=os.environ.get("variable_1"))
	context.perform_gesture('text_entry_no_submit', 'inp_password', grep=os.environ.get("variable_2"))