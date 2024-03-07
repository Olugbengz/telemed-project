from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PatientRecord
from .serializers import PatientRecordSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import permissions

# USERMODEL = get_user_model()



class PatientRecordListCreateView(generics.ListCreateAPIView):
    
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


patient_r_list_create_view = PatientRecordListCreateView.as_view()



class PatientRecordDetails(generics.RetrieveUpdateAPIView):
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer
    lookup_field = 'pk'


patient_r_retrieve_view = PatientRecordDetails.as_view()



class DeletePatientRecord(generics.RetrieveDestroyAPIView):
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer
    lookup_field = 'pk'


patient_r_delete_view = DeletePatientRecord.as_view()