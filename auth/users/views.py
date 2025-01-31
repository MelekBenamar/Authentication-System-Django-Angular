from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user == None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password !')

        payload = {
            'id': user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60), # the token will be expired after 60min
            'iat' : datetime.datetime.utcnow() # set the time when the token has been created to now 
        }

        # create the token using a secret 'secret' and with HS256 algorithm
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        # return the token as cookies:
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        # 'httponly=True' so only the backend can see the token and not the frontend

        return response

# this will get the token from the cookies cause it preserved , otherwise you need to create a token first... that mean login first
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated !')
        
        try:
            payload= jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated !')
        
        user = User.objects.filter(id= payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

# this will delete the token from the cookies  
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data={
            'messages': 'success'
        }
        return response

# For simple endpoints → Use @api_view Function-Based Views (FBVs).
# For scalable, maintainable projects → Use APIView Class-Based Views (CBVs).

