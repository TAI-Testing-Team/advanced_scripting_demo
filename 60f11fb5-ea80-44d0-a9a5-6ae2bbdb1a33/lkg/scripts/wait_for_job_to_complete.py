import logging
import time

def run(context):

    def wait_for_job_to_complete():
        context.perform_gesture('tap', 'btn_complete_job')
        context.verify(labels=["btn_complete_job"], label_count=0)

    context.wait(wait_for_job_to_complete, 40, sleep_in_between=10)    

