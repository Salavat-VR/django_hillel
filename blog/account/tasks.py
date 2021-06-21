from celery import shared_task
from django.core.mail import send_mail

from account.models import User


@shared_task
def send_confirmation_email(user_id):

    user = User.objects.get(id=user_id)

    link = f'/activate/{user.confirmation_token}'
    body = f'To complete the authorization process you have to follow this link: {link}'

    send_mail(
        'The last step',
        body,
        'kyoto.cliche@gmail.com',
        [user.email],
        fail_silently=False,
    )
