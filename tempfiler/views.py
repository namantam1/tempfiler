from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.sites.shortcuts import get_current_site

from .utils import image_uploader

class UploadFileSerializer(serializers.Serializer):
    expire_on = serializers.DateTimeField()
    type = serializers.CharField(max_length=15)
    image = serializers.FileField()


class UploadFile(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            image = serializer.validated_data.get('image')
            typ = serializer.validated_data.get('type')

            response = {
                'file_url': image_uploader.upload(image, typ),
                'site': request.get_full_path()
            }
            return Response(response, status=200)