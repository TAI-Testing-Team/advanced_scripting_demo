'''
This script resets this test so variables are different. It generates a unique email value for use during account creation that is store as a variable that can be recalled in any subsequent test in a test run via a script. Now conditions are reset, you can rerun test and still know it is working.
'''

import logging
import os
from datetime import datetime

log = logging.getLogger(__name__)

# Resetting email same way as before. Generate a datetime string to use as a unique email prefix
username1 = datetime.now().strftime("%Y%m%d-%H%M%S")

# Generate the complete email value and store as a variable
os.environ["variable_1"] = username1 + "@gmail.com"
# Resetting password, so we know that password has been reset to return initial conditions for the test.
os.environ["variable_2"] = "passwordchange"

# To Verify above code
os.environ.get("variable_1")
os.environ.get("variable_2")



def run(context):
	driver=context.get_driver()
	driver.execute_command('RefreshCommand', [])
	context.perform_gesture('text_entry_no_submit', 'inp_email', grep=os.environ.get("variable_1"))
	context.perform_gesture('text_entry_no_submit', 'inp_password', grep=os.environ.get("variable_2"))