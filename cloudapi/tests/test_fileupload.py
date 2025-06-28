import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_protected_fileupload_api():
    # 建立使用者並取得 access token
    user = User.objects.create_user(username='admin', password='admin123')
    client = APIClient()
    login_res = client.post('/api/token/', {
        'username': 'admin',
        'password': 'admin123'
    }, format='json')

    access_token = login_res.data['access']
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

    # 模擬檔案上傳
    file = SimpleUploadedFile("hello.txt", b"hello world", content_type="text/plain")
    response = client.post('/api/upload/', {'file': file}, format='multipart')

    assert response.status_code == 201
    assert 'id' in response.data
