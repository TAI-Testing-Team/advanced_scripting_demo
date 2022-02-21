import logging

log = logging.getLogger(__name__)

def before_each_step():
    properties['num_explore_steps'] += 1
    log.info("Running exploration step: {}".format(properties['num_explore_steps']))
    driver=context.get_driver()
    driver.execute_command('StopAppCommand', ['com.coffye.jrosav'])
    driver.execute_command('LaunchAppCommand', ['com.coffye.jrosav'])

def run(context):
    context.explore(5, before_each_step=before_each_step, ignore_element_errors=True)