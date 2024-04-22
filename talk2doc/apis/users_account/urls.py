from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
# from .views import UserRegistrationView

# router = DefaultRouter()
# router.register('users_account', views.TelemedUserViewSet)
# router.register('doctors', views.DoctorViewSet, basename='doctors')
# router.register('patients', views.PatientViewSet)
# router.register('doctor_profile', views.DoctorProfile)
# router.register('patient_profile', views.PatientProfile)

urlpatterns = [
    # path('', include(router.urls)),
    path('users_account/users', views.users_list_create_view, name='users'),
    path('users_account/doctors', views.doctors_list_create_view, name='doctors-list'),
    path('users_account/patients', views.patients_list_create_view, name='patient-list'),
    path('users_account/users/<int:pk>', views.users_update_destroy_view, name='user_details'),
    path('users_account/doctors/<int:pk>', views.doctors_update_destroy_view, name='doctor_details'),
    path('users_account/patients/<int:pk>', views.patients_update_destroy_view, name='patient_details')
    # path('register', UserRegistrationView.as_view, name='register_user')
    
]