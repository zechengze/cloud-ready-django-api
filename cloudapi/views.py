from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FileUpload, ContactEmail
from .serializers import FileUploadSerializer, ContactEmailSerializer

class FileUploadView(APIView):
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactEmailView(APIView):
    def post(self, request):
        serializer = ContactEmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Email saved successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
