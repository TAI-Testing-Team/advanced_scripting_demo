
import logging
 
def run(context):
    context.verify(labels=["btn_accept"], label_count=0)
    context.perform_gesture('tap', 'btn_verified')