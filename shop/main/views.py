from django.shortcuts import render
from django.shortcuts import redirect
from .models import *


def create(request):
    feedback = Feedback()
    feedback.email = request.POST.get("email")
    feedback.message = request.POST.get("message")
    feedback.save()
    return redirect("/")


def all(request):
    product = Product.objects.all()
    categories = Categories.objects.all()
    CATID = request.GET.get('categories')
    if CATID:
        product = Product.objects.filter(categories=CATID)
    context = {'product': product,
               'categories': categories}
    return render(request, 'main/index.html', context)


def feedback(request):
    return render(request, 'main/feedback.html')