from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from .models import Company
from .forms import CompanyForm

def home(request):
    return render(request,'index.html')

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('index')
    else:
        form = CompanyForm()
    return render(request,'backend/create_company.html',{'form':form})