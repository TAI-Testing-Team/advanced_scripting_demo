import logging
log = logging.getLogger(__name__)

def run(context):
	driver=context.get_driver()
	driver.execute_command('ResizeCommand', [1920, 1080])