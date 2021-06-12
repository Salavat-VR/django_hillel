import pytest

from django.urls import reverse
# @pytest.mark.skip(reason="I wanna skip that")
# def test_skip():
#    pass
#
#
# @pytest.mark.xfail(reason="Obviously wrong output", struct=True)
# def test_fail():
#    assert len("Dmytro") == 6
#
from main.models import ContactUs


def test_home_page(client):
    response = client.get(reverse("home_page"))
    assert response.status_code == 200


def test_contact_us_show(client):
    response = client.get(reverse("contact-us"))
    assert response.status_code == 200


def test_contact_us_post_empty(client):
    response = client.post(reverse("contact-us"))
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.']
    }


def test_contact_us_fill_post(client):
    response = client.post(reverse("contact-us"), data={
        'email': 'dmytro.shashkevych@ukr.net',
        'subject': 'About math',
        'message': 'I am passionate about ...'
    })
    assert response.status_code == 302


def test_contact_us_quantity(client):
    before = ContactUs.objects.count()
    response = client.post(reverse("contact-us"), data={
        'email': 'dmytro.shashkevych@ukr.net',
        'subject': 'About math',
        'message': 'I am passionate about ...'
    })
    assert response.status_code == 302
    assert ContactUs.objects.count() == before + 1
