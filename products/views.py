from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
@api_view (['GET','POST'])
def products_list(request):
    pass

@api_view(['GET','PUT','DELETE'])
def product_detail(request, pk):
    pass