import logging
import json

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.get('http://blogen-inc.surge.sh/dynamic.html')