from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers

from django.utils.timezone import now, localtime
from datetime import timedelta

from .models import MyFile


class UploadFileSerializer(serializers.ModelSerializer):
    def validate_expire_on(self, attrs):
        if attrs < localtime(now()):
            raise serializers.ValidationError(
                "expire on cannot be less than now")

        elif attrs > localtime(now()) + timedelta(days=30):
            raise serializers.ValidationError(
                "cannot store file for more than 30 days")
        return attrs

    class Meta:
        fields = "__all__"
        model = MyFile


class UploadFile(generics.CreateAPIView):
    serializer_class = UploadFileSerializer


class GetFileDelete(generics.RetrieveAPIView, generics.DestroyAPIView):
    serializer_class = UploadFileSerializer
    queryset = MyFile.objects.all()
