from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

User = { "slackUsername": "tekkieware", "backend": True, "age": 25, "bio": "My name is Ozadhe Isaiah and i am a self-taught developer. I can program in a couple of languages and i have deep interest in web development. The aim now is to harness my skills and take it from there." }

print(User)

@api_view(['GET'])
def user_data(request):
    if request.method == 'GET':
        return Response(User)