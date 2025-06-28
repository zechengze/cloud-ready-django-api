import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_login_success():
    # 建立使用者
    User.objects.create_user(username='admin', password='admin123')

    client = APIClient()
    response = client.post('/api/token/', {
        'username': 'admin',
        'password': 'admin123'
    }, format='json')

    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data
