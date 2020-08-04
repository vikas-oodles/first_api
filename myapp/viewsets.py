from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, AddressSerializer, ProfileSerializer
from .models import Profile, Address
from django.contrib.auth.models import User

class ProfileViewsets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewsets(viewsets.ModelViewSet):

    permission_classes = IsAuthenticated,
    queryset = User.objects.all()
    serializer_class = UserSerializer
