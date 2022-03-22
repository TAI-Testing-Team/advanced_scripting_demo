import logging
log = logging.getLogger(__name__)

def run(context):
    def defines_constraints(elem):
        return elem['y'] < 100 and elem['x'] < 1000 
        
    context.explore(3, constraint=defines_constraints)