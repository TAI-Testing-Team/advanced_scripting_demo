import logging
 

def run(context):
    context.verify(labels=["btn_accept"])
    context.perform_gesture('tap', 'btn_accept')