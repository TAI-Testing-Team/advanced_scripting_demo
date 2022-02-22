import logging
log = logging.getLogger(__name__)

def run(context):
    driver=context.get_driver() 
    cookie = driver.execute_command('GetCookieCommand', ['name_of_cookie'])
    log.info('=================cookie info======================')
    log.info(cookie)
