from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework import exceptions


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):


    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        token['trans_company_slug'] = user.username 
        token['trans_company_img'] = user.profile.image.url

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer