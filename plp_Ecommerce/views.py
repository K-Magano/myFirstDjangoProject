from django.shortcuts import render
from .models import Product 
# from django.http import HttpResponse

# Create your views here.
def product_list(request):
    products  = Product.objects.all()
    context = {
        'products': products  
        }
    return render(request,'Ecommerce/product_list.html', context)

# def index(request):
#     return HttpResponse("<h4>Hi from Django</h4>")