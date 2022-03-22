'''
This script generates a unique email value for use during account creation that is stored as a variable
that can be recalled in any subsequent test in a test run via a script.
'''

import logging
import os
from datetime import datetime

log = logging.getLogger(__name__)

# Generate a datetime string to use as a unique email prefix
username1 = datetime.now().strftime("%Y%m%d-%H%M%S")

# Generate the complete email value and store as a variable
os.environ["variable_1"] = username1 + "@testai.com"
# Store a password to use. If password will always be the same this does not need to be done in the script
os.environ["variable_2"] = "Welcome123!"

# To Verify above code
first_variable = os.environ.get("variable_1")
second_variable = os.environ.get("variable_2")

def run(context):
	context.perform_gesture('text_entry_no_submit', 'inp_email', grep=first_variable)
	context.perform_gesture('text_entry_no_submit', 'inp_password', grep=second_variable)