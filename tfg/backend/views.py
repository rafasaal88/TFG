from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from django.views.defaults import page_not_found
from django.contrib.auth import login as do_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib.admin.views.decorators import staff_member_required

#from .models import Company
from .forms import Publicity_Campaign_Form
from .models import Publicity_campaign


def mi_error_404(request, exception):
    return render(request,'backend/404.html')

def mi_error_500(request):
    return render(request,'backend/500.html')



@login_required(login_url='login')
@staff_member_required(login_url='login')
def index(request):
    #company = Company.objects.all().count()
    campaign = Publicity_campaign.objects.all().count()
    users = User.objects.filter(is_staff='False').count()
    return render(request, 'backend/index.html',{'users':users, 'campaign':campaign})


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
def create_publicity_campaign(request):
    if request.method == 'POST':
        form = Publicity_Campaign_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Publicity_Campaign_Form()
    return render(request,'backend/create_publicity_campaign.html',{'form':form})

@login_required(login_url='login')
def list_publicity_campaign(request):
    campaign = Publicity_campaign.objects.all()
    return render(request, 'backend/list_publicity_campaign.html', {'campaign':campaign})

@login_required(login_url='login')
def edit_publicity_campaign(request, id):
    publicity = Publicity_campaign.objects.get(id = id)
    if request.method == 'GET':
        form = Publicity_Campaign_Form(instance = publicity)
    else:
        form = Publicity_Campaign_Form(request.POST, instance = publicity)
        if form.is_valid():
            form.save()
        return redirect ('list_publicity_campaign')
    return render (request, 'backend/edit_publicity_campaign.html', {'form':form})


@login_required(login_url='login')
def delete_publicity_campaign(request, id):
    publicity = Publicity_campaign.objects.get(id = id)
    if request.method == 'POST':
        publicity.delete()
        return redirect('list_publicity_campaign')
    return render(request, 'backend/delete_publicity_campaign.html', {'publicity':publicity})
    

"""


@login_required(login_url='login')
def delete_publicity_campaign(request, id):
    publicity = Publicity_campaign.objects.get(id = id)
    if request.method == 'POST':
        publicity.delete()
        return redirect('list_publicity_campaign')
    return render(request, 'backend/delete_publicity_campaign.html', {'publicity':publicity})
    


@login_required(login_url='login')
def delete_company(request, id):
    company = Company.objects.get(id =id)
    if request.method == 'POST':
        company.delete()
        return redirect('list_company')
    return render(request,'backend/delete_company.html', {'company':company})
"""

@login_required(login_url='login')
def list_users(request):
    users = User.objects.filter(is_staff='False')
    return render(request, 'backend/list_users.html', {'users':users})