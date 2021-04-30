from celery import shared_task

from .models import Logger, Subscriber
from .notify_service import email_send, periodic_email


@shared_task
def notification_by_email(email_to, author):
    email_send(email_to, author)


@shared_task
def deleting_logs():
    Logger.objects.all().delete()
    Logger.save()


@shared_task
def periodic_notification():
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        periodic_email(subscriber.email_to)
