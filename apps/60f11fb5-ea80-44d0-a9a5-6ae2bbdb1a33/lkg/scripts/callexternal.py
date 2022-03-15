import logging
from taplink import tapstep
from input_text import typetext


log = logging.getLogger(__name__)

def run(context):
    tapstep(context)
    typetext(context)