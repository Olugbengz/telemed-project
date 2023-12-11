from rest_framework import serializers
from .models import PatientRecord
from django.contrib.auth import get_user_model
from django.conf import settings
# from apis.users_account.models import Patient
# from apis.users_account.serializers import PatientSerializer
USERMODEL = get_user_model()

class PatientRecordSerializer(serializers.HyperlinkedModelSerializer):
    record_owner = serializers.ReadOnlyField(source='record_owner.fullname')
    record_owner_id = serializers.PrimaryKeyRelatedField(queryset=USERMODEL.objects.all(), source='record_owner', write_only=True, allow_null=True)

    class Meta:
        model = PatientRecord
        fields = [
            'record_owner',
            'record_owner_id',
            'medical_condition',
            'allergies',
            'current_medication',
            'lab_test',
            'test_result',
            'prescription',
            'new_appointment', 
            'note',
            'referral',
        ]

   