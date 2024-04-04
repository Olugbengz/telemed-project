from rest_framework import serializers
from .models import TeleMedUser, Doctor, Patient, DocAvailableDate
from apis.patient_record.serializers import PatientRecordSerializer
from apis.patient_record.models import PatientRecord
from django.conf import settings


# class DocSpecialtySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DocSpecialty
#         fields = ['specialty']

USERMODEL = settings.AUTH_USER_MODEL

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    doctor = serializers.ReadOnlyField(source='doctor.fullname')
    # doctor_id = serializers.PrimaryKeyRelatedField(queryset=USERMODEL.objects.all(), source='doctor', write_only=True, allow_null=True)

    class Meta:
        model = Doctor
        fields = [
            'id',
            # 'email', 
            # 'first_name', 
            # 'last_name', 
            # 'phone',
            'doctor',
            'specialty', 
            'language', 
            'location', 
            'hospital', 
            'years_of_experience', 
            'about', 
            'profile_image'
        ]
        
class PatientSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.ReadOnlyField(source='patient.fullname')

    class Meta:
        model = Patient
        fields = [
            'id',
            'patient',
            'gender',
            'alternative_phone',
            'emergency_contact_name',
            'emergency_contact_phone',
            'emergency_contact_relationship',
            'medical_plan',
            'profile_image',
            # 'patient_record',
        ]
    
    # def create(self, validated_data):
    #     patient_record_data = validated_data.pop('patient_record')        
    #     patient = self.Meta.model(**validated_data)
    #     for record in patient_record_data:
    #         PatientRecord.objects.create(patient=patient, **record)        
    #     patient.save()
    #     return patient

class TelemedUserSerializer(serializers.HyperlinkedModelSerializer):
    # doctor = DoctorSerializer()
    # patient = PatientSerializer()
    
    
    class Meta:
        model = TeleMedUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):         
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)               
        user.save()
        return user
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
        






# doctor_data = validated_data.pop('doctor')
# patient_data = validated_data.pop('patient')   
        
# Doctor.objects.create(user=user, **doctor_data)
# Patient.objects.create(user=user, **patient_data)

# doctor = instance.doctor
# patient = instance.patient 


# General user info
# instance.email = validated_data.get('email', instance.email)
# instance.first_name = validated_data.get('first_name', instance.first_name)
# instance.last_name = validated_data.get('last_name', instance.last_name)
# instance.phone = validated_data.get('phone', instance.phone)
# instance.save()

# Doctor specific info
# Doctor_data = Doctor_data.pop(doctor)
# instance.doctor.language = Doctor_data['language']
# instance.doctor.location = Doctor_data['location']
# instance.doctor.hospital = Doctor_data['hospital']
# instance.doctor.years_of_experience = Doctor_data['years_of_experience']
# instance.doctor.about = Doctor_data['about']        
# instance.doctor.profile_image = Doctor_data['profile_image']
# instance.doctor.save()

# Patient specific info
# patient_data = validated_data.pop(patient)
# instance.patient.gender = patient_data['gender']
# instance.patient.alternative_phone = patient_data['alternative_phone']
# instance.patient.emergency_contact_name = patient_data['emergency_contact_name']
# instance.patient.emergency_contact_phone = patient_data['emergency_contact_phone']
# instance.patient.emergency_contact_relationship = patient_data['emergency_contact_relationship']
# instance.patient.medical_plan = patient_data['medical_plan']        
# instance.patient.save()         

# Create Patient Record
# pat_record_data = validated_data.pop(patient_record)
# instance.patient_record.record_owner = pat_record_data['record_owner']
# instance.patient_record.medical_condition = pat_record_data['medical_condition']
# instance.patient_record.allergies = pat_record_data['allergies']
# instance.patient_record.current_medication = pat_record_data['current_medication']
# instance.patient_record.lab_test = pat_record_data['lab_test']
# instance.patient_record.test_result = pat_record_data['test_result']
# instance.patient_record.prescription = pat_record_data['prescription']
# instance.patient_record.new_appointment = pat_record_data['new_appointment']
# instance.patient_record.note = pat_record_data['note']
# instance.patient_record.referral = pat_record_data['referral']