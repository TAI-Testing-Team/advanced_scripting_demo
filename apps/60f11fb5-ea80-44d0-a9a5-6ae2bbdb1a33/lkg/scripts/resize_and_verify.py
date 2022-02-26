import logging
log = logging.getLogger(__name__)

def run(context):
	driver=context.get_driver()
	context.get_all_elements()
	driver.execute_command('ResizeCommand', [800, 600])
	context.verify(labels=["lnk_find_element_800_600"])
	driver.execute_command('ResizeCommand', [1920, 1080])
	context.verify(labels=['lnk_find_element'])