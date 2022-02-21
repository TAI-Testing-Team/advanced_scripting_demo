import logging

log = logging.getLogger(__name__)

def before_each_step():
        properties['num_explore_steps'] += 1
        log.info("Running exploration step: {}".format(properties['num_explore_steps']))
        driver.launch_app(http://blogen-inc.surge.sh)

context.explore(20, before_each_step=before_each_step, ignore_element_errors=True)