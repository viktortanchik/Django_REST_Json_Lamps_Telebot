from django.shortcuts import render
from .forms import SubscriberForm
from .models import Subscriber
import os.path
from .csvW import CSV_W
####
####
def index(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST":
        print(os.path)
        print(request.POST)
        new_form = form.save()
        data = form.cleaned_data
        print(form.cleaned_data)
        print(data["name"])
        name = data["name"]
        print(data["SN"])
        sn = data["SN"]
        print(sn)
        print(name)
        CSV_W(name,sn)
        all = Subscriber.objects.all()
    form = SubscriberForm()
    return render(request, 'login/login.html', locals())

def page_1(request):
    return render(request, 'login/page_1.html', locals())

def setup_lamp(request):
    return render(request, 'login/setup_lamp.html', locals())

def contact(request):
    return render(request, 'login/contact.html', locals())
def products(request):
    return render(request, 'login/products.html', locals())


