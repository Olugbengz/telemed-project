from django.urls import path, include



urlpatterns = [
    
    path('', include('apis.users_account.urls')),
    path('patient_record/', include('apis.patient_record.urls')),
]