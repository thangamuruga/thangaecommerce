from django.shortcuts import render
from .models import catagory
from .models import product

# Create your views here.

def home(request):
	products = product.objects.all()
	return render(request, "test/index.html",context = {"products":products})
