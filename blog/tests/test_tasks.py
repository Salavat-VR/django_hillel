from main.models import Author
from main.tasks import notification_by_email, deleting_logs


def test_notification_by_email(client, faker_fixture):
    """
    check whether email con be sent from random email to any of Authors
    """
    notification_by_email(faker_fixture.email(), Author.objects.all().order_by("?").first())


def test_deleting_logs():
    deleting_logs()
