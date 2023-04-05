from django.shortcuts import render
from home.models import Product

# Create your views here.
def home(request):
    contexts = Product.objects.all()
    return render(request,"home.html",{
        "contexts":contexts
    })