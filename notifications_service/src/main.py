import time
from multiprocessing import Pool

from core.logger import logger
from core.settings import get_settings
from core.worker import create_worker
from models.queues import Queues

STARTUP_WAITING_SECS = 15


def main():
    settings = get_settings()
    queues = []
    queues += [Queues.email_low_priority.value] * settings.workers.low_priority_email_n_workers
    queues += [Queues.email_medium_priority.value] * settings.workers.medium_priority_email_n_workers
    queues += [Queues.email_high_priority.value] * settings.workers.high_priority_email_n_workers

    logger.info(f'Waiting for application startup for {STARTUP_WAITING_SECS} secs')
    time.sleep(STARTUP_WAITING_SECS)

    with Pool(len(queues)) as p:
        p.map(create_worker, queues)


if __name__ == '__main__':
    main()
