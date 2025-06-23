from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from cloudapi.models import FileUpload, ContactEmail

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_file_upload(self):
        file_data = SimpleUploadedFile("test.txt", b"file_content")
        response = self.client.post('/api/upload/', {'file': file_data, 'description': 'test file'}, format='multipart')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(FileUpload.objects.count(), 1)

    def test_contact_email(self):
        data = {
            "name": "小吉",
            "email": "chi@example.com",
            "subject": "吉",
            "message": "測試訊息"
        }
        response = self.client.post('/api/contact/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ContactEmail.objects.count(), 1)
