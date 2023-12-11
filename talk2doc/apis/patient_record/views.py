from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PatientRecord
from .serializers import PatientRecordSerializer
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
# USERMODEL = get_user_model()

# @api_view(['GET', 'POST'])
# def patient_record_list(request):
#     patients_record = PatientRecord.objects.all()
#     data = {}
#     if patients_record:
#         data = model_to_dict(patients_record)
#     return JsonResponse(data)

class PatientRecordListCreateView(generics.ListCreateAPIView):
    
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer


patient_r_list_create_view = PatientRecordListCreateView.as_view()


# class PatientRecordDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = PatientRecord.objects.all()
#     serializer_class = PatientRecordSerializer