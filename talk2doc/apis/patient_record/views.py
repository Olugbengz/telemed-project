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
# from django.forms.models import model_to_dict

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(record_owner=self.request.user)
    #     return super().perform_create(serializer)


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