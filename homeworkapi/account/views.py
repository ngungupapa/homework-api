from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from account.serializers import RegistrationSerializer, LoginSerializer, ChangePasswordSerializer
from rest_framework.authtoken.models import Token
from account.models import Account
from django.contrib.auth import login, authenticate, logout

# Create your views here.
@api_view(['POST', ])
@permission_classes([AllowAny])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['username'] = account.username
			# token = Token.objects.get(user=account).key
			# data['token'] = token
		else:
			data = serializer.errors
		return Response(data)

@api_view(['POST', ])
@permission_classes([AllowAny])
def Login_view(request):

    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            email = serializer.data['email']
            password = serializer.data['password']
            email = Account.objects.filter(email=email).first()
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                token = Token.objects.get(user=email).key
                data['token'] = token
                return Response(data)
            else:
                return Response('Invalid email or password!')

@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def Logout_view(request):
    users = request.user
    request.user.auth_token.delete()
    Token.objects.create(user=users)
    logout(request)
    if request.user.is_authenticated:
        return Response('Logging out Unsuccessful!')
    else:
        return Response('Logging out Successful!')

@api_view(['POST', ])
@permission_classes([IsAuthenticated])
def chgpass_view(request):
    
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        res = {}
        users = request.user
        if serializer.is_valid():
            # check if user type correct current password
            if not users.check_password(serializer.data['password_cur']):
                res['status'] = 'Failed'
                res['message'] = 'Current password is wrong!'
                return Response(res)
            else:
                users.set_password(serializer.data['password_new'])
                res['status'] = 'Success'
                res['message'] = 'Password was updated!'
                Token.objects.filter(user=users).delete()
                Token.objects.create(user=users)
                users.save()
                return Response(res)
        else:
            return Response('Request is invalid')

