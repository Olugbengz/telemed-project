from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.user_list_create_view, name='telemeduser'),
    path('login/', views.signin, name='login'),
    
]