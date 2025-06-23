from django.urls import path
from .views import FileUploadView, ContactEmailView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('contact/', ContactEmailView.as_view(), name='contact-email'),
]
