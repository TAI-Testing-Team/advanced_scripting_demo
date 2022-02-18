import logging

log = logging.getLogger(__name__)

def run(context):
	driver=context.get_driver()
	driver.execute_command('StopAppCommand', ['com.coffye.jrosav'])
	driver.execute_command('LaunchAppCommand', ['com.coffye.jrosav'])