# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import viewsets
# from django.views import APIView
from .models import Doctor, Patient, DoctorProfile, PatientProfile, DocAvailableDate
from .serializers import (
    DoctorProfileSerializer, 
    DoctorProfileSerializer, 
    PatientProfileSerializer, 
    PatientProfileSerializer, 
    TeleMedUserSerializer
    )



USERMODEL = get_user_model()


class TeleMedUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = USERMODEL.objects.all()
    serializer_class = TeleMedUserSerializer

users_list_create_view = TeleMedUserListCreateAPIView.as_view()

class TeleMedUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = USERMODEL.objects.all()
    serializer_class = TeleMedUserSerializer

users_update_destroy_view = TeleMedUserRetrieveUpdateDestroyAPIView.as_view()

class DoctorProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

doctors_list_create_view = DoctorProfileListCreateAPIView.as_view()

class DoctorProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

doctors_update_destroy_view = DoctorProfileRetrieveUpdateDestroyAPIView.as_view()

class PatientProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer

patients_list_create_view = PatientProfileListCreateAPIView.as_view()

class PatientProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer

patients_update_destroy_view = PatientProfileRetrieveUpdateDestroyAPIView.as_view()





# class TelemedUserViewSet(viewsets.ModelViewSet):
    
#     queryset = USERMODEL.objects.all()
#     serializer_class = TelemedUserSerializer
    # session_authentication = [authentication.SessionAuthentication]
    # permission_classes = [IsAdminUser]


# class DoctorListCreateView(generics.ListCreateAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer


# doctor_list_create_view = DoctorListCreateView.as_view()


# class PatientListCreateView(generics.ListCreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

# patient_list_create_view = PatientListCreateView.as_view()


# class UserRegistrationView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         reg_serilizer = TelemedUserSerializer(data=request.data)
#         if reg_serilizer.is_valid():
#             user = reg_serilizer.save()
#             if user:
#                 return Response(status=status.HTTP_400_201_CREATED)
#         return Response(reg_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
