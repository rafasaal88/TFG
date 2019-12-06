from django.shortcuts import render, redirect
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

def list_company(request):
    company = Company.objects.all()
    context = {'company':company}
    return render(request, 'backend/list_company.html', context)

def edit_company(request, id):
    company = Company.objects.get(id =id)
    if request.method == 'GET':
        form = CompanyForm(instance = company)
    else:
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'backend/create_company.html', {'form':form})

def delete_company(request, id):
    company = Company.objects.get(id =id)
    if request.method == 'POST':
        company.delete()
        return redirect('index')
    return render(request,'backend/delete_company.html', {'company':company})
