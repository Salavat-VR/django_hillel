from django.contrib.sites import requests


def notify(email_to, author_name):
    email_send(email_to, author_name)
    # telegram_notify(email_to)


def email_send(email_to, author):
    from django.core.mail import send_mail

    send_mail(
        'urgent notification email',
        'Deat customer! You have subscribed on Author: {}'.format(author.name),
        'kyoto.cliche@gmail.com',
        [email_to],
        # fail_silenty=False,
    )


def periodic_email(email_to):
    from django.core.mail import send_mail

    send_mail(
        'Email at 9 pm',
        '{}'.format(requests.get('https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php')),
        'kyoto.cliche@gmail.com',
        [email_to],
        # fail_silenty=False,
    )


def telegram_notify():
    pass