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
from .forms import Publicity_Campaign_Form, User_Form_Email, User_Form_Name, User_Profile_Form, User_Profile_Create, Product_Form, Product_Form_Edit, Publicity_Campaign_Form_Edit
from .models import Publicity_campaign, UserProfile, Product


#Mostrar error 404
def mi_error_404(request, exception):
    return render(request,'backend/404.html')


#Mostrar error 500
def mi_error_500(request):
    return render(request,'backend/500.html')


#Mostrar index del backend
@login_required(login_url='user_login')
@staff_member_required(login_url='user_login')
def index(request):
    #company = Company.objects.all().count()
    campaign = Publicity_campaign.objects.all().count()
    users = User.objects.filter(is_staff='False').count()
    products = Product.objects.filter(available='True').count()
    return render(request, 'backend/index.html',{'users':users, 'campaign':campaign, 'products':products})


#Loguear usuario
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


#Cerrar sesión de usuario
def user_logout(request):
    # Finalizamos la sesión
    django_logout(request)
    # Redireccionamos a la portada
    return redirect('user_login')


###############################################################################################
################################ Publicity Campaign CRUD Methods ##############################
###############################################################################################


#Crear campaña de publicidad
@login_required(login_url='user_login')
def publicity_campaign_create(request):
    user_profile = request.user
    user_profile_name = user_profile.username
    if request.method == 'POST':
        form = Publicity_Campaign_Form(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = user_profile_name
            form.save()
            return redirect('publicity_campaign_list')
    else:
        form = Publicity_Campaign_Form(initial={'user': user_profile_name})
        form.fields['product'].queryset = Product.objects.filter(available = 'True')  # for example
    return render(request,'backend/publicity_campaign_create.html',{'form':form})


#Mostrar campaña de publicidad
@login_required(login_url='user_login')
def publicity_campaign(request, id):
    campaign = Publicity_campaign.objects.get(id = id)
    return render(request, 'backend/publicity_campaign.html', {'campaign':campaign})

#Mostrar campaña de publicidad
@login_required(login_url='user_login')
def publicity_campaign_complete(request, id):
    campaign = Publicity_campaign.objects.get(id = id)
    return render(request, 'backend/publicity_campaign_complete.html', {'campaign':campaign})



#Listar todas las campañas de publicidad
@login_required(login_url='user_login')
def publicity_campaign_list(request):
    campaign = Publicity_campaign.objects.all()
    return render(request, 'backend/publicity_campaign_list.html', {'campaign':campaign})


#Editar campaña de publicidad
@login_required(login_url='user_login')
def publicity_campaign_edit(request, id):
    publicity = Publicity_campaign.objects.get(id = id)
    if request.method == 'GET':
        form = Publicity_Campaign_Form_Edit(instance = publicity)
    else:
        form = Publicity_Campaign_Form_Edit(request.POST, request.FILES, instance = publicity)
        if form.is_valid():
            form.save()
        return redirect ('publicity_campaign_list')
    return render (request, 'backend/publicity_campaign_edit.html', {'form':form, 'publicity':publicity})


#Eliminar campaña de publicidad
@login_required(login_url='user_login')
def publicity_campaign_delete(request, id):
    publicity = Publicity_campaign.objects.get(id = id)
    if request.method == 'POST':
        publicity.delete()
        return redirect('publicity_campaign_list')
    return render(request, 'backend/publicity_campaign_delete.html', {'publicity':publicity})


###############################################################################################
########################## User Methods #######################################################
###############################################################################################


#Listar usuarios que no son administradores
@login_required(login_url='user_login')
def users_list(request):
    users = User.objects.filter(is_staff='False')
    return render(request, 'backend/users_list.html', {'users':users})


#Vista para ver el perfil del usuario logueado
@login_required(login_url='user_login')
def user_profile_admin(request):
    return render(request, 'backend/user_profile_admin.html')


#Vista para el perfil del resto de usuarios
@login_required(login_url='user_login')
def user_profile(request, id):
    user_profile = User.objects.get(id = id)
    return render(request, 'backend/user_profile.html', {'user_profile':user_profile})


#Vista para editar el perfil del resto de usuarios
@login_required(login_url='user_login')
def user_profile_edit(request, id):
    user_profile = User.objects.get(id = id)
    return render(request, 'backend/user_profile_edit.html', {'user_profile':user_profile})


#Editar email del usuario pasado por referencia
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


#Editar nombre y apellidos del usuario pasado por referencia
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


#editar imagen de perfil del usuario pasado por referencia
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


#Crear un nuevo usuario no administrador
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


#Eliminar el usuario pasado por referencia
@login_required(login_url='user_login')
def user_delete(request, id):
    user_profile = User.objects.get(id = id)
    if request.method == 'POST':
        user_profile.delete()
        return redirect('users_list')
    if request.method == 'GET':
        if user_profile.is_staff:
            return render(request, 'backend/user_delete_error.html', {'user_profile':user_profile})
        else:
            return render(request, 'backend/user_delete.html', {'user_profile':user_profile})

###############################################################################################
########################## Product Methods ####################################################
###############################################################################################


#Añadir nuevo producto
@login_required(login_url='user_login')
def product_create(request):
    if request.method == 'POST':
        form = Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user.username
            form.save()
            return redirect('product_list')
    else:
        form = Product_Form()
        return render(request, 'backend/product_create.html', {'form':form})


#Listar productos
@login_required(login_url='user_login')
def product_list(request):
    product = Product.objects.all().filter(available='True')
    return render(request, 'backend/product_list.html', {'product':product})


#Ver producto
@login_required(login_url='user_login')
def product(request, id):
    product = Product.objects.get(id = id)
    return render(request, 'backend/product.html', {'product':product})

#Editar precio
def product_edit_price(request, id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':        
        precio = float(request.POST.get("newprice"))     
        product.available = 'False'
        product.save()
        product_new = Product.objects.create(name=product.name, price = precio)
        product_new.description = product.description
        product_new.user = request.user.username
        product_new.image = product.image
        product_new.save()
        return redirect('product_list')
    else:
        return render(request, 'backend/product_edit_price.html', {'product':product})


#Deshabilitar producto
@login_required(login_url='user_login')
def product_disable(request, id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        product.available = 'False'
        product.save()
        return redirect('product_list')
    else:
        return render(request, 'backend/product_disable.html', {'product':product})


@login_required(login_url='user_login')
def product_edit(request, id):
    product = Product.objects.get(id = id)
    if request.method == 'GET':
        form = Product_Form_Edit(instance = product)
        return render(request, 'backend/product_edit.html', {'product':product, 'form':form})
    else:
        form = Product_Form_Edit(request.POST, request.FILES, instance = product)
        if form.is_valid():
            form.instance.available = 'False'
            form.save()
            if request.POST.get("newprice"):
                product_new = Product.objects.create(name=product.name, price = float(request.POST.get("newprice")))
            else:
                product_new = Product.objects.create(name=product.name, price = product.price)
            product_new.description = product.description
            product_new.user = request.user.username
            product_new.image = product.image
            product_new.save()
            return redirect('product_list')