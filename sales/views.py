from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Products, Textile


def index(request):
    latest_products = Products.objects.order_by('-Price')
    latest_textile = Textile.objects.all()
    context = {
        'latest_products': latest_products,
        'latest_textile': latest_textile

    }
    return render(request, 'sales/index.html', context)
