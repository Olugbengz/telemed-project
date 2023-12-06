from rest_framework import serializers
from .models import TeleMedUser, DocSpecialty, Doctor, Patient, DocAvailableDate


class DocSpecialtySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocSpecialty
        fields = ['specialty']

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    specialty = DocSpecialtySerializer()
    class Meta:
        model = Doctor
        fields = [
            'specialty', 
            'language', 
            'location', 
            'hospital', 
            'years_of_experience', 
            'about', 
            'profile_image'
        ]
        
class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'patient_record',
            'gender',
            'alternative_phone',
            'emergency_contact_name',
            'emergency_contact_phone',
            'emergency_contact_relationship',
            'medical_plan',
            'profile_image'
        ]

class TelemedUserSerializer(serializers.HyperlinkedModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()

    class Meta:
        model = TeleMedUser
        fields = ['email', 
                'first_name', 
                'last_name', 
                'phone',
                'is_staff', 
                'is_active',
                'is_admin', 
                'doctor',
                'patient',
                ]

    def create(self, validated_data):
        doctor_data = validated_data.pop('doctor')
        patient_data = validated_data.pop('patient')
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)
        Doctor.objects.create(user=user, **doctor_data)
        Patient.objects.create(user=user, **patient_data)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        doctor = instance.doctor
        patient = instance.patient 

        # General user info
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()

        # Patient specific info
        Doctor_data = Doctor_data.pop(doctor)
        instance.doctor.language = Doctor_data['language']
        instance.doctor.location = Doctor_data['location']
        instance.doctor.hospital = Doctor_data['hospital']
        instance.doctor.years_of_experience = Doctor_data['years_of_experience']
        instance.doctor.about = Doctor_data['about']        
        instance.doctor.profile_image = Doctor_data['profile_image']
        instance.doctor.save()

        # Patient specific info
        patient_data = validated_data.pop(patient)
        instance.patient.patient_record = patient_data['patient_record']
        instance.patient.gender = patient_data['gender']
        instance.patient.alternative_phone = patient_data['alternative_phone']
        instance.patient.emergency_contact_name = patient_data['emergency_contact_name']
        instance.patient.emergency_contact_phone = patient_data['emergency_contact_phone']
        instance.patient.emergency_contact_relationship = patient_data['emergency_contact_relationship']
        instance.patient.medical_plan = patient_data['medical_plan']
        # instance.profile_image = patient_data['profile_image']
        instance.patient.save()         

        return super().update(instance, validated_data)
    
    