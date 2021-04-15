from celery import shared_task
from time import sleep

@shared_task
def notification_by_email(wait=10):
    print("Dmyrto" * 4)
