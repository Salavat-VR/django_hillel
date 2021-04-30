from django.contrib.sites import requests

from .models import Author


def notify(email_to, author_name):
    email_send(email_to, author_name)
    # telegram_notify(email_to)


def email_send(email_to, author):
    from django.core.mail import send_mail

    send_mail(
        'urgent notification email',
        f'Dear customer! You have subscribed on Author: {Author.objects.all().get(pk=author)}',
        'kyoto.cliche@gmail.com',
        [email_to],
        fail_silently=False,
    )


def periodic_email(email_to):
    from django.core.mail import send_mail

    send_mail(
        'Email at 9 pm',
        '{}'.format(requests.get('https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php')),
        'kyoto.cliche@gmail.com',
        [email_to],
        # fail_silently=False,
    )


def telegram_notify():
    pass
