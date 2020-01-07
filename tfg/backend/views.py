from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from django.contrib.auth import login as do_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.admin.views.decorators import staff_member_required

from .models import Company
from .forms import CompanyForm




@login_required(login_url='login')
@staff_member_required(login_url='login')
def index(request):
    company = Company.objects.all().count()
    users = User.objects.filter(is_staff='False').count()
    return render(request, 'backend/index.html',{'company':company, 'users':users})


def login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'backend/index.html')
        else:
            django_logout(request)
            return render(request, 'backend/user_not_staff.html')
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
                return redirect('index')

    # Si llegamos al final renderizamos el formulario
    return render(request, 'backend/login.html', {'form': form})


def logout(request):
    # Finalizamos la sesión
    django_logout(request)
    # Redireccionamos a la portada
    return redirect('login')


@login_required(login_url='login')
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CompanyForm()
    return render(request,'backend/create_company.html',{'form':form})



@login_required(login_url='login')
def list_company(request):
    company = Company.objects.all()
    return render(request, 'backend/list_company.html', {'company':company} )



@login_required(login_url='login')
def edit_company(request, id):
    company = Company.objects.get(id =id)
    if request.method == 'GET':
        form = CompanyForm(instance = company)
    else:
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
        return redirect('list_company')
    return render(request,'backend/edit_company.html', {'form':form})


@login_required(login_url='login')
def delete_company(request, id):
    company = Company.objects.get(id =id)
    if request.method == 'POST':
        company.delete()
        return redirect('list_company')
    return render(request,'backend/delete_company.html', {'company':company})


@login_required(login_url='login')
def list_users(request):
    users = User.objects.filter(is_staff='False')
    return render(request, 'backend/list_users.html', {'users':users})