'''
This script generates a unique email value for use during account creation that is store as a variable
that can be recalled in any subsequent test in a test run via a script.
'''

import logging
import os
import time
from datetime import datetime

log = logging.getLogger(__name__)

# Generate a datetime string to use as a unique email prefix
username1 = datetime.now().strftime("%Y%m%d-%H%M%S")

# Generate the complete email value and store as a variable
os.environ["variable_1"] = username1 + "@gmail.com"
# Store a password to use. If password will always be the same this does not need to be done in the script
os.environ["variable_2"] = "passwordchange"

# To Verify above code
os.environ.get("variable_1")
os.environ.get("variable_2")



def run(context):
	driver=context.get_driver()
	driver.execute_command('RefreshCommand', [])
	context.perform_gesture('text_entry_no_submit', 'inp_email', grep=os.environ.get("variable_1"))
	context.perform_gesture('text_entry_no_submit', 'inp_password', grep=os.environ.get("variable_2"))