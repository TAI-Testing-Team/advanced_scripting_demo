import logging


log = logging.getLogger(__name__)


def run(context):
    driver = context.get_driver()
    try:
        driver.dismiss_alert(ignore_errors=True)
    except:
        pass
