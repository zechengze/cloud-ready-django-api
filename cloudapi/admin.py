from django.contrib import admin
from .models import FileUpload, ContactEmail

@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    search_fields = ('description',)

@admin.register(ContactEmail)
class ContactEmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
