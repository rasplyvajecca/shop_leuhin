from django.shortcuts import render
from django.shortcuts import redirect
from .models import *


def create(request):
    feedback = Message()
    feedback.email = request.POST.get("email")
    feedback.message = request.POST.get("message")
    feedback.save()
    return redirect("/")


def all(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    if CATID == '1':
        product = Product.objects.filter(categories=CATID)
        context = {'product': product,
               'categories': categories}
        return render(request, 'product/men.html', context)
    elif CATID == '2':
        product = Product.objects.filter(categories=CATID)
        context = {'product': product,
               'categories': categories}
        return render(request, 'product/women.html', context)
    elif CATID == '3':
        product = Product.objects.filter(categories=CATID)
        context = {'product': product,
               'categories': categories}
        return render(request, 'product/children.html', context)
    context = {'product': product,
               'categories': categories}
    return render(request, 'product/index.html', context)


def feedback(request):
    return render(request, 'product/feedback.html')