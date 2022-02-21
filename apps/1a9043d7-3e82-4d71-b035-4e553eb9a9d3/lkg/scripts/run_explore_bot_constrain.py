import logging
log = logging.getLogger(__name__)

def run(context):
    def constraint(elem):
        return elem['y'] > 1200
    context.explore(10, constraint=constraint)
