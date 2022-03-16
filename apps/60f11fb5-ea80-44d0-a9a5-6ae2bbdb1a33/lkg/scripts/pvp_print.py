import logging
import json

log = logging.getLogger(__name__)

def run(context):
    script_vals = context.get_test_script_vals()
    json_string = json.dumps(script_vals)
    context.perform_gesture('text_entry_no_submit', 'inp_test_info', json_string)

    # Can retrieve a value within a subsequently executed script.
    # log.info("=========================================INFORMATION==================================")
    # log.info(script_vals)
    # log.info("=========================================INFORMATION==================================")
