import logging
import json

log = logging.getLogger(__name__)

def run(context):
    element_info = context.find_element('btn_coordinate_tap')
    json_string = json.dumps(element_info)
    # parseable_unicode = json.loads(json_string)



    #This code used to see info in terminal
    log.info('====================output find element====================')
    log.info(element_info)
    log.info('====================end find element====================')