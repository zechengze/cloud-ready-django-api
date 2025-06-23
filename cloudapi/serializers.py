from rest_framework import serializers
from .models import FileUpload, ContactEmail

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['id', 'file', 'description', 'uploaded_at']

class ContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']
