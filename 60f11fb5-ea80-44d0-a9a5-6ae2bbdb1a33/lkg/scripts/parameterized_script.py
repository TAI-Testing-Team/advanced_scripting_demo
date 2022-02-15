import logging
import json
from csv import DictReader
log = logging.getLogger(__name__)



def run(context):

    input = context.get_input()
    input_param_csv = context.get_file_path("resources/input_params_step.csv")

    my_label_input = input['my_label']
    my_text_input = input['my_text']

    # context.perform_gesture('text_entry_no_submit', my_label, my_text)
