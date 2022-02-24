'''
This script generates a unique email value for use during account creation that is stored as a variable
that can be recalled in any subsequent test in a test run via a script.
Change YOUR_DOMAIN to a valid email domain.
Also make sure 'inp_email' matches the label name used in the test.ai GUI for the email field if needed.
'''

import logging
import os
import time
from datetime import datetime

log = logging.getLogger(__name__)

# Generate a datetime string to use as a unique email prefix
username1 = datetime.now().strftime("%Y%m%d-%H%M%S")

# Generate the complete email value and store as a variable
os.environ["unique_email"] = "testai-" + username1 + "@gmail.com"

def run(context):
    context.perform_gesture('text_entry_no_submit', 'inp_text_entry', grep= os.environ.get("unique_email"))
    context.verify(grep=os.environ["unique_email"])
    context.perform_gesture('tap', 'btn_submit')
