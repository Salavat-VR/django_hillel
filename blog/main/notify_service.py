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


def telegram_notify():
    pass
