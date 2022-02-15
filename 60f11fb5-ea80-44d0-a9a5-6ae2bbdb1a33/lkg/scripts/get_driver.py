import logging
import json

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.get('http://google.com')

    # Can retrieve a value within a subsequently executed script.
    log.info("=========================================INFORMATION==================================")
    log.info(driver)
    log.info("=========================================INFORMATION==================================")
