from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from django.contrib.auth import login as do_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout

from .models import Company
from .forms import CompanyForm

def home(request):
    if request.user.is_authenticated:
        return render(request, 'backend/index.html')
    # En otro caso redireccionamos al login
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return render(request, 'backend/index.html')
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return HttpResponseRedirect('index')

    # Si llegamos al final renderizamos el formulario
    return render(request, 'backend/login.html', {'form': form})


def logout(request):
    # Finalizamos la sesión
    django_logout(request)
    # Redireccionamos a la portada
    return redirect('login')



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
