from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PersonSerializer

from .models import Person

import time

# Create your views here.


d = [{'age': 4, 'legs': 6}, {'age': 3, 'legs': 8}, {'age': 5, 'legs': 7} ]



class GetView(APIView):
    def get(self, request) -> Response:
        t = time.time()
        return Response(status=status.HTTP_200_OK, data=t)

def hello(request):
    return HttpResponse('hello')


class PersonView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer



