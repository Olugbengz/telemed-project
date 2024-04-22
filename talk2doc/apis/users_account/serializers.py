from rest_framework import serializers
from .models import TeleMedUser, Doctor, DoctorProfile, Patient, PatientProfile, DocAvailableDate
from django.conf import settings
# from apis.patient_record.serializers import PatientRecordSerializer
# from apis.patient_record.models import PatientRecord



class TeleMedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeleMedUser
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'role', 'profile_image']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'role', 'profile_image']

class DoctorProfileSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=False)
    class Meta:
        model = DoctorProfile
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Patient
        fields = '__all__'

class PatientProfileSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many=False)
    class Meta:
        model = PatientProfile
        fields = '__all__'
    

#  Update Doctor's Account Profile
# class DoctorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = '__all__'

       
    # def create(self, validated_data):         
    #     doc_profile_data = validated_data.pop('doctor')  
    #     doctor = Doctor.objects.create(**validated_data)
    #     DoctorProfile.objects.create(doctor=doctor, **doc_profile_data)
    #     return Patient    

    
# class DoctorProfileSerializer(serializers.ModelSerializer):
#     doctor = DoctorSerializer(many=False)
   
#     class Meta:
#         model = DoctorProfile
#         fields = '__all__'


# Update Patient's Account Profile
# class PatientSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Patient
#         fields = '__all__'

# class PatientProfileSerializer(serializers.ModelSerializer):
#     patient = PatientSerializer(many=False)
#     class Meta:
#         model = PatientProfile
#         fields = '__all__'

    # def create(self, validated_data): 
    #     patient_profile_data = validated_data.pop('patient')  
    #     patient = Patient.objects.create(**validated_data)
    #     PatientProfile.objects.create(patient=patient, **patient_profile_data)
    #     return Patient 

      
       


# Create All Users Including Admins, And Members Of Staff, Will Use Django's Built-in Group Feature

# class TelemedUserSerializer(serializers.ModelSerializer):
    
    
#     class Meta:
#         model = TeleMedUser
#         fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'profile_image', 'base_role']

#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):         
#         password = validated_data.pop('password', None)
#         user = self.Meta.model(**validated_data)

#         if password is not None:
#             user.set_password(password)               
#         user.save()
#         return user
    
#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)
        
        


#######################################################################
        #  BELOW LINES OF CODE WILL BE REVIEWED IN THE FUTURE 
#######################################################################


# class DocSpecialtySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DocSpecialty
#         fields = ['specialty']

# USERMODEL = settings.AUTH_USER_MODEL


# class DocSpecialtySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DocSpecialty
#         fields = ['specialty']

# USERMODEL = settings.AUTH_USER_MODEL


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

#####################################################
# Response fron ChatGPT
#####################################################

# from .models import TeleMedUser, DoctorProfile, PatientProfile

