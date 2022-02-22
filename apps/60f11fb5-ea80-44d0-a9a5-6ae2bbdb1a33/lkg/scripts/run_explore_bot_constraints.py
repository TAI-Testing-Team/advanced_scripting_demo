import logging
log = logging.getLogger(__name__)

def run(context):
    def constraint(elem):
        return elem['y'] < 30
    context.explore(5, constraint=constraint)
