def run(context):
    def before_each_step():
        driver = context.get_driver()
        driver.execute_command('StopAppCommand', ['com.coffye.jrosav'])
        driver.execute_command('LaunchAppCommand', ['com.coffye.jrosav'])   
    context.explore(5, before_each_step=before_each_step, ignore_element_errors=True)