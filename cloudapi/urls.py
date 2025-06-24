from django.urls import path, include
from .views import FileUploadView, ContactEmailView
from rest_framework.routers import DefaultRouter
from .views import FileUploadViewSet

router = DefaultRouter()
router.register(r'files', FileUploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('contact/', ContactEmailView.as_view(), name='contact-email'),
]
