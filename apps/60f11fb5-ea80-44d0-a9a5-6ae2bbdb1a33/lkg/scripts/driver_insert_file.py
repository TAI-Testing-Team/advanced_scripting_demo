#This script is still marked yellow. Still need to update this script to match the docs, but we need a way to upload a file. Right now it just saves the csv file as a variable and calls it.


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