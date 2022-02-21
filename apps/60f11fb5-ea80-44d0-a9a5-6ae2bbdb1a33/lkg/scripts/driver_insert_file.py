'''
This script browses to a file and select it.
Useful for file upload fields.
This example is for a csv file but can be modified for any file type.
Replace <your csv file path or name> with the path to the appropriate file, or the file name if the file is in the same directory as this script file.
'''

import logging
import time

log = logging.getLogger(__name__)


def run(context):

    driver = context.get_driver()
    time.sleep(2)
    csv_file = context.get_file_path('insert_file/my_csv_file.csv')

    log.info('=============================csv file info==============================')
    log.info(csv_file)
    log.info('=============================csv file info==============================')

    context.perform_gesture('text_entry_no_submit', 'inp_test_info', csv_file)

    log.info('CSV upload successful.')