# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework import authentication, generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Doctor, Patient, DocAvailableDate
from .serializers import DoctorSerializer, PatientSerializer, TelemedUserSerializer



USERMODEL = get_user_model()


class TelemedUserViewSet(viewsets.ModelViewSet):
    
    queryset = USERMODEL.objects.all()
    serializer_class = TelemedUserSerializer
    # session_authentication = [authentication.SessionAuthentication]
    # permission_classes = [IsAdminUser]

   


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes = [IsAuthenticated]

    # def get_object(self, queryset=None, **kwargs):
    #     doc = self.kwargs.get('pk')
    #     return get_object_or_404(USERMODEL, doctor=doc)

    # def get_queryset(self):
    #     return 


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsAuthenticated]




# class TelemedUserDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = USERMODEL.objects.all()
#     serializer_class = TelemedUserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serilizer = TelemedUserSerializer(data=request.data)
        if reg_serilizer.is_valid():
            user = reg_serilizer.save()
            if user:
                return Response(status=status.HTTP_400_201_CREATED)
        return Response(reg_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
