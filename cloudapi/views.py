from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import FileUpload, ContactEmail
from .serializers import FileUploadSerializer, ContactEmailSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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

class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="取得所有檔案上傳紀錄",
        responses={200: FileUploadSerializer(many=True)},
        manual_parameters=[
        openapi.Parameter('filename', openapi.IN_QUERY, description="檔案名稱", type=openapi.TYPE_STRING)
    ]
    )
    def list(self, request, *args, **kwargs):
        """列出所有檔案上傳紀錄"""
        return super().list(request, *args, **kwargs)
