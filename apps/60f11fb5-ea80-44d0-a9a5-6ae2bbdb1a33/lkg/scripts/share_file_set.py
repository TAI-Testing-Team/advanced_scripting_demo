import logging
from csv import DictReader
import requests
import json

log = logging.getLogger(__name__)

def run(context):

# 1: open file:

    # get path to local file:
    csv_path = context.get_file_path("insert_file/my_csv_file.csv")

    # extract data from csv file as JSON:
    csv_data = []
    with open(csv_path) as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            # you can also interact with rows directly using row.get('<key>')
            csv_data.append(row)

# 2: access context datastore and add data for use in subsequent test steps:

    # access the internal test case datastore (part of the `context` object)
    script_vals = context.get_test_script_vals()

    # add extracted data to the TC datastore for use in subsequent steps
    script_vals['csv_data'] = csv_data
    string = json.dumps(csv_data)

    context.perform_gesture('text_entry_no_submit', 'inp_test_info', string)

