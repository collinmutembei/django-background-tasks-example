from background_task import background
from logging import getLogger

logger = getLogger(__name__)

@background(schedule=60)
def demo_task(message):
    logger.debug('demo_task. message={0}'.format(message))
