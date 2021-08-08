from celery.decorators import task
from upload_service import UploadService
import logging

logger = logging.getLogger("custom_logger")


@task(bind=True, name="save_products_to_db", default_retry_delay=60, retry_kwargs={'max_retries': 3}, queue="products_queue")
def save_products_to_db(self, file_path):
    """sends an email """
    try :
        product_upload =  UploadService(file_path)
        product_upload.save()
        logger.info("uploaded with  celery %s", file_path)
        return 'uploaded {}'.format(file_path)
    except Exception as exc:
        logger.exception('Celery task failure!!!1', exc_info=exc)
        raise self.retry(exc=exc, countdown=60)