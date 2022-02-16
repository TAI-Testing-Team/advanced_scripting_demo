import logging

log = logging.getLogger(__name__)


def run(context):
	driver=context.get_driver()
	cookies = driver.execute_command('GetAllCookiesCommand', [])
	log.info('=============================cookie time========================================')
	log.info(cookies)