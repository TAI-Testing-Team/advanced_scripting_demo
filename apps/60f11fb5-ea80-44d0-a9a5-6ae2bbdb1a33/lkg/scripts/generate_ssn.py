'''
This script generates a random valid ssn which should help with account creation where needed.
Make sure to change the 2 instances of 'inp_ssn' to the label name used in the test.ai GUI if that is not what was used for the ssn field.
'''

import logging
import time
import os
import random

log = logging.getLogger(__name__)
random.seed(time.perf_counter())

def run(context):
    if element_exists(context, 'inp_text_entry'):
        random_area = random.randint(100, 600)
        random_group = random.randint(1, 99)
        random_serial = random.randint(1, 9999)
        random_ssn = '{0}{1:02d}{2:04d}'.format(random_area, random_group, random_serial)
        context.perform_gesture('text_entry_no_submit', 'inp_text_entry', random_ssn)
        context.verify(grep=random_ssn)
        context.perform_gesture('tap', 'btn_submit')

def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0