'''
This starts Bot mode restricted to certain coordinates on the screen.
The bot only interacts with elements in the boundaries.
This script specifies 30 steps, that can be adjusted as needed.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    def constraint(elem):
        return elem['y'] < 100 and elem['x'] < 1000 
        
    context.explore(3, constraint=constraint)