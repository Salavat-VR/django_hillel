import requests
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
from main.forms import PostForm
from main.models import ContactUs, Post

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


def test_contact_us_fill_post(client, faker_fixture):
    response = client.post(reverse("contact-us"), data={
        'email': faker_fixture.email(),
        'subject': faker_fixture.word(),
        'message': faker_fixture.word()
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


def test_valid_form(client, faker_fixture):
    some_random_words = requests.get('https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php').text
    artificial_post = Post(title=faker_fixture.word(), description=faker_fixture.word(), content=some_random_words)
    data = {
            'title': artificial_post.title,
            'description': artificial_post.description,
            'content': artificial_post.content
            }
    form = PostForm(data=data)
    assert form.is_valid()
