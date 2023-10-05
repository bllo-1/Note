from django.contrib.auth.models import User

def test_home_view(client):
    response = client.get(path='/')
    assert response.status_code == 200
    

def test_signup(client):
    response = client.get(path='/signup')
    assert response.status_code == 200
    assert 'home/register.html' in response.template_name


def test_signup_authenticated(client):
    user = User.objects.create_user()
    response = client.get(path='/signup')
    assert response.status_code == 200
    assert 'note/notes_list.html' in response.template_name        