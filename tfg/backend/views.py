from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from django.views.defaults import page_not_found

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



@login_required(login_url='login_user')
@staff_member_required(login_url='login_user')
def index(request):
    #company = Company.objects.all().count()
    campaign = Publicity_campaign.objects.all().count()
    users = User.objects.filter(is_staff='False').count()
    return render(request, 'backend/index.html',{'users':users, 'campaign':campaign})


def login_user(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('index')
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
            username = request.POST['username']
            password = request.POST['password']

            # Verificamos las credenciales del usuario
            user = authenticate(request, username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                login(request, user)
                # Y le redireccionamos a la portada
                if request.user.is_active:
                    return redirect('index')
                else:
                    return render(request, 'backend/user_not_active.html') #esto no funciona aun

    # Si llegamos al final renderizamos el formulario
    return render(request, 'backend/login.html', {'form': form})

def logout(request):
    # Finalizamos la sesión
    django_logout(request)
    # Redireccionamos a la portada
    return redirect('login_user')





###############################################################################################
################################ Publicity Campaign CRUD Methods ##############################
###############################################################################################

@login_required(login_url='login_user')
def create_publicity_campaign(request):
    if request.method == 'POST':
        form = Publicity_Campaign_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_publicity_campaign')
    else:
        form = Publicity_Campaign_Form()
    return render(request,'backend/create_publicity_campaign.html',{'form':form})



@login_required(login_url='login_user')
def list_publicity_campaign(request):
    campaign = Publicity_campaign.objects.all()
    return render(request, 'backend/list_publicity_campaign.html', {'campaign':campaign})

@login_required(login_url='login_user')
def list_publicity_campaign_edit(request):
    campaign = Publicity_campaign.objects.all()
    return render(request, 'backend/list_publicity_campaign_edit.html', {'campaign':campaign})

@login_required(login_url='login_user')
def list_publicity_campaign_delete(request):
    campaign = Publicity_campaign.objects.all()
    return render(request, 'backend/list_publicity_campaign_delete.html', {'campaign':campaign})

@login_required(login_url='login_user')
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

@login_required(login_url='login_user')
def delete_publicity_campaign(request, id):
    publicity = Publicity_campaign.objects.get(id = id)
    if request.method == 'POST':
        publicity.delete()
        return redirect('list_publicity_campaign')
    return render(request, 'backend/delete_publicity_campaign.html', {'publicity':publicity})


###############################################################################################
###############################################################################################
###############################################################################################






@login_required(login_url='login_user')
def list_users(request):
    users = User.objects.filter(is_staff='False')
    return render(request, 'backend/list_users.html', {'users':users})

@login_required(login_url='login_user')
def profile(request):
    #user_login = request.user
    #user = User.objects.filter(id= user_login.id)
    return render(request, 'backend/profile.html')



