from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Doctor, Patient, DocAvailableDate
from .serializers import DoctorSerializer, PatientSerializer, TelemedUserSerializer
from rest_framework import generics


USERMODEL = get_user_model()


class TelemedUserListCreateView(generics.ListCreateAPIView):
    
    queryset = USERMODEL.objects.all()
    serializer_class = TelemedUserSerializer


user_list_create_view = TelemedUserListCreateView.as_view()


class TelemedUserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = USERMODEL.objects.all()
    serializer_class = TelemedUserSerializer



def signin(request):
    pass