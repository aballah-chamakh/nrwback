from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,status,generics
from .models import User,Profile
from .serializers import UserSerializer,ProfileSerializer
from .permissions import IsOwnerOrNone,PostOnly

      #"formik": "^2.2.1",
      #"jquery": "^3.5.1",
      #"jwt-decode": "^3.0.0",
      #"node-sass": "^4.14.1",
      #"react-awesome-modal": "^2.0.5",
      #"react-spinners": "^0.9.0",
      #"redux": "^4.0.5",
      #"yup": "^0.29.3",
      #"react-redux": "^7.2.2",
      #"react-router-dom": "^5.2.0" */
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (PostOnly,)
  



class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = (IsOwnerOrNone,)
    lookup_field = 'slug'
    
    def get_queryset(self):
        if not(self.request.user.is_authenticated) : 
            return []
        user_obj = self.request.user
        qs = Profile.objects.filter(user=user_obj)
        return qs








