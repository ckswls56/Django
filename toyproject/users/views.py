from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

# Create your views here.
@permission_classes([AllowAny])
class RegisterView(APIView):
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = TokenObtainPairSerializer.get_token(user)
            access_token = str(token.access_token)
            refresh_token = str(token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "User created successfully",
                    "access_token": access_token,
                    "refresh_token": refresh_token
                },
                status=status.HTTP_201_CREATED,
            )
            res.set_cookie("access_token",access_token, httponly=True)
            res.set_cookie("refresh_token",refresh_token, httponly=True)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        res = Response(
            {
                "message": "User logged out successfully"
            },
            status=status.HTTP_200_OK,
        )
        res.delete_cookie("access_token")
        res.delete_cookie("refresh_token")
        return res