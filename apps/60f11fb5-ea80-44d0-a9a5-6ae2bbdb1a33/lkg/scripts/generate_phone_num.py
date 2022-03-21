'''
This script generates a US phone number with a valid area code and exchange (3 digits after the area code).
Make sure to change the 2 instances of inp_phone_number to the label name used in the test.ai GUI if that is not what was used for the phone number field.
Copy both this file and the 'us-area-code-cities.csv' file from the share drive directory to the lkg/scripts directory.
'''

import logging
import time
import random
import csv

log = logging.getLogger(__name__)
col = 0
random.seed(time.perf_counter())

def run(context):
    # gather info
        us_area_code_cities = context.get_file_path("us-area-code-cities.csv")
    
    # find a valid area code
        with open(us_area_code_cities, encoding="utf-8") as f:
            reader = csv.reader(f)
            data = [row[col] for row in reader]
        # generate valid phone number and take action
        if element_exists(context, 'inp_text_entry'):
            random_area_code = random.choice(data)
            random_exchange = random.randint(200, 999)
            random_number = random.randint(1, 9999)
            random_phone_number = '{0}{1:03d}{2:04d}'.format(random_area_code, random_exchange, random_number)
            context.perform_gesture('text_entry_no_submit', 'inp_text_entry', random_phone_number)
            context.verify(grep=random_phone_number)
            context.perform_gesture('tap', 'btn_submit')
        
def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0