import logging


def run(context):
        context.verify(grep="numb3r str1ng")
        context.perform_gesture('tap', 'btn_numbers')