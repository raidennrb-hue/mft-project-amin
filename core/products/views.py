from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import Product
# Create your views here.
def PGET(request):
    return JsonResponse(list(Product.objects.all().values()), safe=False)
def PPOST(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(name=data['name'], price=data['price'])
        return JsonResponse({'message': 'Product added', 'id': product.id}, status=201)
    return JsonResponse({'error': 'POST only'}, status=405)