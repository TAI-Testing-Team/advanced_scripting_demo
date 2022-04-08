import logging


log = logging.getLogger(__name__)


def run(context):
    find_elements_value = context.find_elements_with_label('btn_tap')


    log.info('<==================================================================>')
    log.info(find_elements_value)
    log.info('<==================================================================>')


