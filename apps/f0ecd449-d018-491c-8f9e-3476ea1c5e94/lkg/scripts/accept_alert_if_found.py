# from codecs import ignore_errors
# from lib2to3.pgen2 import driver
import logging


log = logging.getLogger(__name__)

# This script will accept a native system alert for Web or iOS. 
# In this script there is an ignore_errors=True flag which acts as a "run if label found". 
# If the alert appears, it will accept it and the test will not fail if it doesn't appear.


def run(context):
    driver = context.get_driver()
    try:
        driver.accept_alert(ignore_errors=True)
    except:
        pass        
