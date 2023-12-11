from django.urls import path
from . import views


urlpatterns = [
    path('', views.patient_r_list_create_view, name='patient_record'),
    # path('', views.patient_record_list, name='patient_record'),
   
    
]