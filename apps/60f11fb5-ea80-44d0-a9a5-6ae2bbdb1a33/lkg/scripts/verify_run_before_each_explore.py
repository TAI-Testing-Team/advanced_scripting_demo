import logging
log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.get('http://blogen-inc.surge.sh/findelem.html')
    context.get_all_elements()
    context.perform_gesture('text_entry_no_submit','inp_ta_element_info','Run Before Each Explore Step Test - SUCCESS')