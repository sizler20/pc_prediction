from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(["GET", "POST"])
def prediction_response(request):
    
    data = {
        'prediction': 'mac OS'
    }

    return Response(data)


