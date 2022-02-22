def run(context):
	driver=context.get_driver()
	driver.execute_command('DeleteAllCookiesCommand', [])