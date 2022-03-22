import logging
from script_organization import myscript_organized

log = logging.getLogger(__name__)

''' Tests out "Script Organization" - This script calls the script (myscript_organized.py)in the subfolder of script_organization which is inside the lkg/scripts folder '''

def run(context):
    myscript_organized.run(context)
    