
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Rolex
from .serializer import RolexSerializer
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from functools import reduce


@api_view(['GET'])
def getRolexWatches(request):
    products = Rolex.objects.filter(goLive='yes')
    serializer = RolexSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRolex(request, pk):
    product = Rolex.objects.get(_id=pk)
    serializer = RolexSerializer(product, many=False)
    return Response(serializer.data)