from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import re

# Create your views here.

User = { "slackUsername": "tekkieware", "backend": True, "age": 25, "bio": "My name is Ozadhe Isaiah and i am a self-taught developer. I can program in a couple of languages and i have deep interest in web development. The aim now is to harness my skills and take it from there." }


@api_view(['GET'])
def user_data(request):
    if request.method == 'GET':
        return Response(User)


@api_view(['POST'])
def calculate(request):
    data = request.data
    operation_type = str(data['operation_type'])
    try:
        first_number = data['x']
    except KeyError:
        first_number = ''
    try:
        second_number = data['y']
    except KeyError:
        first_number = ''
    message = ''    
    #addition logic
    if operation_type.strip().lower() == 'addition' or operation_type.strip().lower().__contains__('addition') or operation_type.strip().lower().__contains__('add') or operation_type.strip().lower().__contains__('adding') or operation_type.strip().lower().__contains__('plus'):
        #when numbers are given
        if first_number and second_number:
            result = first_number + second_number
        else:
            #string is given
            numbers = re.findall('[0-9,-]+', operation_type.strip().lower())
            try:
                first_number = int(numbers[0])
                second_number = int(numbers[1])
                operation_type = 'addition'
                result = first_number + second_number
            except IndexError:
                message = 'Please provide two valid numbers'          
    #subtraction logic     
    elif operation_type.strip() == 'subtraction' or operation_type.strip().lower().__contains__('subtraction') or operation_type.strip().lower().__contains__('subtract') or operation_type.strip().lower().__contains__('minus') or operation_type.strip().lower().__contains__('subtracting'):
        #numbers are given
        if first_number and second_number:
            result = first_number - second_number
        else:
            #string is given
            numbers = re.findall('[0-9,-]+', operation_type.strip().lower())
            try:
                first_number = int(numbers[0])
                second_number = int(numbers[1])
                operation_type = 'subtraction'
                result = first_number - second_number
            except IndexError:
                message = 'Please provide two valid numbers'
    #multiplication logic
    elif operation_type.strip() == 'multiplication' or operation_type.strip().lower().__contains__('multiplication') or operation_type.strip().lower().__contains__('multiply') or operation_type.strip().lower().__contains__('multiplying') or operation_type.strip().lower().__contains__('times'):
        #numbers are given
        if first_number and second_number:
            result = first_number * second_number
        else:
            #string is given
            numbers = re.findall('[0-9,-]+', operation_type.strip().lower())
            try:
                first_number = int(numbers[0])
                second_number = int(numbers[1])
                operation_type = 'multiplication'
                result = first_number * second_number
            except IndexError:
                message = 'Please provide two valid numbers'
    
    if message:
        Result = {"slackUsername": "tekkieware", "message": 'ERROR ' + message }
    else:
        Result = {"slackUsername": "tekkieware", "result": result, "operation_type": operation_type }

    return Response(Result)
