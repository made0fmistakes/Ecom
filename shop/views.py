from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)
    # products=Product.objects.all()
    # print(products)
    # n=len(products)
    # nSlides= n//4 + ceil((n/4)-(n//4))
    # allprods=[[products, range(1,nSlides), nSlides],
    #         [products, range(1,nSlides), nSlides]]
    # params={'allprods':allprods}
    # # params={'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # return render(request,'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return HttpResponse('this is contact section of shop')

def tracker(request):
    return HttpResponse('this is tracker section of shop')

def search(request):
    return HttpResponse('this is search section of shop')

def productView(request):
    return HttpResponse('this is productView section of shop')

def checkout(request):
    return HttpResponse('this is checkout section of shop')
