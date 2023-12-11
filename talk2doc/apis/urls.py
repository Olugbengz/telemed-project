from django.urls import path, include
from .views import home


urlpatterns = [
    path('', home, name='home'),
    path('users_account/', include('apis.users_account.urls')),
    path('patient_record/', include('apis.patient_record.urls')),
]