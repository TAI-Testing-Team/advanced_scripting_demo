import logging

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    url = driver.execute_script('return window.location.href;')
    context.perform_gesture('text_entry_no_submit', 'inp_test_info', url)





    # url is set as variable, print it to the log output for visual check
    # log.info('====================script start====================')
    # log.info(url)
    # log.info('====================script end======================')