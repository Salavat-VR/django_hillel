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


def test_home_page(client):
    response = client.get(reverse("home_page"))
    assert response.status_code == 200
