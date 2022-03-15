import logging
from script_organization import myscript_organized

log = logging.getLogger(__name__)

def run(context):
    myscript_organized.run(context)
    