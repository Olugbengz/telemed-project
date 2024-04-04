from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserRegistrationView

router = DefaultRouter()
router.register('users_account', views.TelemedUserViewSet)
router.register('doctors', views.DoctorViewSet, basename='doctors')
router.register('patients', views.PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', UserRegistrationView.as_view, name='register_user')
    
]