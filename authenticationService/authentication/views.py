import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserRegisterSerializer
from .models import User

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Login' : '/login/',
        'Logout' : '/logout/',
        'Signup' : '/signup/',
        'Profile' : '/profile/',
    }

    return Response(api_urls)


@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']

    user = User.objects.filter(username=username).first()

    if user is None:
        raise AuthenticationFailed('User not found!')

    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password!')

    payload = {
        'email': user.email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret-app-key', algorithm='HS256')

    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)

    response.data = {
        'jwt': token
    }

    return response


@api_view(['POST'])
def signup(request):
    js_data = request.data
    serializer = UserRegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    payload = {
        'email': js_data['email'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret-app-key', algorithm='HS256')

    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)

    response.data = {
        'jwt': token
    }

    return response


@api_view(['POST'])
def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }

    return response


@api_view(['GET'])
def profile(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('You are not logged in! Or Token Expired Log in again.')

    try:
        payload = jwt.decode(token, 'secret-app-key', algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('En error!')

    user = User.objects.filter(email=payload['email']).first()
    serializer = UserSerializer(user)

    return Response(serializer.data)
