import logging
log = logging.getLogger(__name__)

def run(context):
    def constraint(elem):
        return elem['y'] < 100 and elem['x'] < 1000 
        
    context.explore(3, constraint=constraint)