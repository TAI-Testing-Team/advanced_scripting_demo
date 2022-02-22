def run(context):
	driver=context.get_driver()
	driver.execute_command('ModifyCookieCommand', ['cookie_name', 'cookie_value'])