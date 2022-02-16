import logging

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    url = context.get_driver().execute_script('return window.location.href;')
    
    # url is set as variable, print it to the log output for visual check
    log.info('====================script start====================')
    log.info(url)
    log.info('====================script end======================')