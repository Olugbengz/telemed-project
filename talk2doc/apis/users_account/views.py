from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Doctor, Patient, DocAvailableDate
from .serializers import DoctorSerializer, PatientSerializer, TelemedUserSerializer
from rest_framework import authentication, generics, permissions


USERMODEL = get_user_model()


class TelemedUserListCreateView(generics.ListCreateAPIView):
    
    queryset = USERMODEL.objects.all()
    serializer_class = TelemedUserSerializer
    session_authentication = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


user_list_create_view = TelemedUserListCreateView.as_view()


class TelemedUserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = USERMODEL.objects.all()
    serializer_class = TelemedUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



def signin(request):
    pass