from lib2to3.pgen2 import driver
import logging


log = logging.getLogger(__name__)

# This script will accept a native system alert for Web or iOS. 


def run(context):
    context.get_driver()
    try:
        driver.accept_alert()
    except:
        pass        
