from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class LoginTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tokens = serializer.validated_data
        access_token = tokens['access']
        refresh_token = tokens['refresh']

        response = Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        response.set_cookie(key='access_token', value=access_token, httponly=True)
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)

        return response