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
from .forms import Publicity_Campaign_Form, User_Form_Email, User_Form_Name, User_Profile_Form, User_Profile_Create
from .models import Publicity_campaign, UserProfile


def mi_error_404(request, exception):
    return render(request,'backend/404.html')

def mi_error_500(request):
    return render(request,'backend/500.html')



@login_required(login_url='user_login')
@staff_member_required(login_url='user_login')
def index(request):
    #company = Company.objects.all().count()
    campaign = Publicity_campaign.objects.all().count()
    users = User.objects.filter(is_staff='False').count()
    return render(request, 'backend/index.html',{'users':users, 'campaign':campaign})


def user_login(request):
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

def user_logout(request):
    # Finalizamos la sesión
    django_logout(request)
    # Redireccionamos a la portada
    return redirect('user_login')





###############################################################################################
################################ Publicity Campaign CRUD Methods ##############################
###############################################################################################




@login_required(login_url='user_login')
def publicity_campaign_create(request):
    user_profile = request.user
    if request.method == 'POST':
        form = Publicity_Campaign_Form(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['user'] = user_profile.username
            form.save()
            return redirect('publicity_campaign_list')
    else:
        form = Publicity_Campaign_Form(initial={'user': user_profile.username})
    return render(request,'backend/publicity_campaign_create.html',{'form':form})


@login_required(login_url='user_login')
def publicity_campaign(request, id):
    campaign = Publicity_campaign.objects.get(id = id)
    return render(request, 'backend/publicity_campaign.html', {'campaign':campaign})



@login_required(login_url='user_login')
def publicity_campaign_list(request):
    campaign = Publicity_campaign.objects.all()
    return render(request, 'backend/publicity_campaign_list.html', {'campaign':campaign})



@login_required(login_url='user_login')
def publicity_campaign_edit(request, id):
    publicity = Publicity_campaign.objects.get(id = id)
    if request.method == 'GET':
        form = Publicity_Campaign_Form(instance = publicity)
    else:
        form = Publicity_Campaign_Form(request.POST, instance = publicity)
        if form.is_valid():
            form.save()
        return redirect ('publicity_campaign_list')
    return render (request, 'backend/publicity_campaign_edit.html', {'form':form})

@login_required(login_url='user_login')
def publicity_campaign_delete(request, id):
    publicity = Publicity_campaign.objects.get(id = id)
    if request.method == 'POST':
        publicity.delete()
        return redirect('publicity_campaign_list')
    return render(request, 'backend/publicity_campaign_delete.html', {'publicity':publicity})


###############################################################################################
###############################################################################################
###############################################################################################


@login_required(login_url='user_login')
def users_list(request):
    users = User.objects.filter(is_staff='False')
    return render(request, 'backend/users_list.html', {'users':users})


#Vista para el usuario logueado
@login_required(login_url='user_login')
def user_profile_admin(request):
    return render(request, 'backend/user_profile_admin.html')

#Vista para el resto de usuarios
@login_required(login_url='user_login')
def user_profile(request, id):
    user_profile = User.objects.get(id = id)
    return render(request, 'backend/user_profile.html', {'user_profile':user_profile})

#Vista para el resto de usuarios
@login_required(login_url='user_login')
def user_profile_edit(request, id):
    user_profile = User.objects.get(id = id)
    return render(request, 'backend/user_profile_edit.html', {'user_profile':user_profile})

@login_required(login_url='user_login')
def user_edit_email(request, id):
    user_profile = User.objects.get(id = id)
    if request.method == 'GET':
        form = User_Form_Email(instance = user_profile)
    else:
        form = User_Form_Email(request.POST, instance = user_profile)
        if form.is_valid():
            form.save()
        if request.user.id == user_profile.id:
            return redirect ('user_profile_admin')
        else:
            return redirect ('user_profile_edit', id)
    return render (request, 'backend/user_edit_email.html', {'form':form, 'user_profile':user_profile})

@login_required(login_url='user_login')
def user_edit_name(request, id):
    user_profile = User.objects.get(id = id)
    if request.method == 'GET':
        form = User_Form_Name(instance = user_profile)
    else:
        form = User_Form_Name(request.POST, instance = user_profile)
        if form.is_valid():
            form.save()
        if request.user.id == user_profile.id:
            return redirect ('user_profile_admin')
        else:
            return redirect ('user_profile_edit', id)
    return render (request, 'backend/user_edit_name.html', {'form':form, 'user_profile':user_profile})


@login_required(login_url='user_login')
def user_edit_picture(request, id):
    user_profile = User.objects.get(id = id)
    userprofile = UserProfile.objects.get (user = user_profile)
    if request.method == 'GET':
        form = User_Profile_Form(instance = userprofile)
    else:
        form = User_Profile_Form(request.POST, request.FILES, instance = userprofile)
        if form.is_valid():
            form.save()
        if request.user.id == user_profile.id:
            return redirect ('user_profile_admin')
        else:
            return redirect ('user_profile_edit', id)
    return render (request, 'backend/user_edit_picture.html', {'form':form, 'user_profile':user_profile})

@login_required(login_url='user_login')
def user_create(request):
    if request.method == 'POST':
        form = User_Profile_Create(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            user = User.objects.get(username = username)
            UserProfile.objects.create(user = user)    
            return redirect ('users_list')
    else:
        form = User_Profile_Create()
        return render(request, 'backend/user_create.html', {'form':form})

