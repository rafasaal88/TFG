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
from django.utils import timezone
from datetime import datetime


from .forms import Publicity_Campaign_Form, User_Form_Email, User_Form_Name, User_Profile_Form, User_Profile_Create, Product_Form, Product_Form_Edit, Recipe_Form, Tag_nfc_Form 


from .models import Publicity_campaign, UserProfile, Product, Product_history, Recipe, Tag_nfc


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
    users_admin = User.objects.filter(is_staff='True').count()
    products = Product.objects.count()
    recipes = Recipe.objects.count()
    tags = Tag_nfc.objects.count()
    return render(request, 'backend/index.html',{'users':users, 'campaign':campaign, 'products':products, 'recipes': recipes, 'users_admin':users_admin, 'tags':tags})


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
    campaign = Publicity_campaign.objects.all().order_by('id').reverse()
    return render(request, 'backend/publicity_campaign_list.html', {'campaign':campaign})


#Editar campaña de publicidad
@login_required(login_url='user_login')
def publicity_campaign_edit(request, id):
    publicity = Publicity_campaign.objects.get(id = id)
    if request.method == 'GET':
        form = Publicity_Campaign_Form(instance = publicity)
    else:
        form = Publicity_Campaign_Form(request.POST, request.FILES, instance = publicity)
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
    users = User.objects.filter(is_staff='False').order_by('id').reverse()
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
def user_disable(request, id):
    user_profile = User.objects.get(id = id)
    if request.method == 'POST':
        user_profile.is_active= 'False'
        user_profile.save()
        return redirect('users_list')
    if request.method == 'GET':
        if user_profile.is_staff:
            return render(request, 'backend/user_disable_error.html', {'user_profile':user_profile})
        else:
            return render(request, 'backend/user_disable.html', {'user_profile':user_profile})



#Eliminar el usuario pasado por referencia
@login_required(login_url='user_login')
def user_enable(request, id):
    user_profile = User.objects.get(id = id)
    if request.method == 'POST':
        user_profile.is_active= 'True'
        user_profile.save()
        return redirect('users_list')
    if request.method == 'GET':
        if user_profile.is_staff:
            return render(request, 'backend/user_enable_error.html', {'user_profile':user_profile})
        else:
            return render(request, 'backend/user_enable.html', {'user_profile':user_profile})





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
    product = Product.objects.all().order_by('id').reverse()
    return render(request, 'backend/product_list.html', {'product':product})


#Ver producto
@login_required(login_url='user_login')
def product(request, id):
    product = Product.objects.get(id = id)
    return render(request, 'backend/product.html', {'product':product})


#Ver producto
@login_required(login_url='user_login')
def product_history(request, id):
    product = Product_history.objects.get(id = id)
    return render(request, 'backend/product_history.html', {'product':product})


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


#Hhabilitar producto
@login_required(login_url='user_login')
def product_enable(request, id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        product.available = 'True'
        product.save()
        return redirect('product_list')
    else:
        return render(request, 'backend/product_enable.html', {'product':product})


#Editar producto
@login_required(login_url='user_login')
def product_edit(request, id):
    product_original = Product.objects.get(id = id)
    product = Product.objects.get(id = id)
    if request.method == 'GET':
        form = Product_Form_Edit(instance = product)
        return render(request, 'backend/product_edit.html', {'product':product, 'form':form})
    else:
        form = Product_Form_Edit(request.POST, request.FILES, instance = product)
        if form.is_valid():
            form.instance.date = datetime.now()
            if request.POST.get("newprice"):
                form.instance.price = request.POST.get("newprice")
            else:
                form.instance.price = product.price
            ProductOld = Product_history.objects.create(product = product_original, price = product_original.price, date = product_original.date)
            ProductOld.name = product_original.name
            ProductOld.description = product_original.description
            ProductOld.available = False
            ProductOld.unit = product_original.unit
            ProductOld.user = product_original.user
            ProductOld.image = product_original.image
            ProductOld.save()
            form.save()
            return redirect('product_list')


#Listar productos
@login_required(login_url='user_login')
def product_list_history(request, id):
    product = Product.objects.get(id = id)
    product_history = Product_history.objects.filter(product = id).order_by('date').reverse()
    return render(request, 'backend/product_list_history.html', {'product':product, 'product_history':product_history})





###############################################################################################
########################## Recipe Methods #####################################################
###############################################################################################


#Crear recetas
@login_required(login_url='user_login')
def recipe_create(request):
    if request.method == 'POST':
        form = Recipe_Form(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user.username
            form.save()
            return redirect('recipe_list')
    else:
        form = Recipe_Form()
        return render(request, 'backend/recipe_create.html', {'form':form})


#Listar recetas
@login_required(login_url='user_login')
def recipe_list(request):
    recipe = Recipe.objects.all().order_by('id').reverse()
    return render(request, 'backend/recipe_list.html', {'recipe':recipe})


#Ver receta
@login_required(login_url='user_login')
def recipe(request, id):
    recipe = Recipe.objects.get(id = id)
    return render(request, 'backend/recipe.html', {'recipe':recipe})


#Editar receta
@login_required(login_url='user_login')
def recipe_edit(request, id):
    recipe = Recipe.objects.get(id = id)
    if request.method == 'GET':
        form = Recipe_Form(instance = recipe)
    else:
        form = Recipe_Form(request.POST, request.FILES, instance = recipe)
        if form.is_valid():
            form.instance.date = datetime.now()
            form.instance.user = request.user.username
            form.save()
        return redirect ('recipe_list')
    return render (request, 'backend/recipe_edit.html', {'form':form, 'recipe':recipe})



#Eliminar receta
@login_required(login_url='user_login')
def recipe_delete(request, id):
    recipe = Recipe.objects.get(id = id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'backend/recipe_delete.html', {'recipe':recipe})



###############################################################################################
########################## NFT_TAG METHODS ####################################################
###############################################################################################


#Crear tag
@login_required(login_url='user_login')
def tag_nfc_create(request):
    if request.method == 'POST':
        form = Tag_nfc_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_nfc_list')
    else:
        form = Tag_nfc_Form()
        return render(request, 'backend/tag_nfc_create.html', {'form':form,})


#Listar tags
@login_required(login_url='user_login')
def tag_nfc_list(request):
    tag_nfc = Tag_nfc.objects.all().order_by('id').reverse()
    return render(request, 'backend/tag_nfc_list.html', {'tag_nfc':tag_nfc})


#Deshabilitar tag
@login_required(login_url='user_login')
def tag_nfc_disable(request, id):
    tag_nfc = Tag_nfc.objects.get(id = id)
    if request.method == 'POST':
        tag_nfc.available = 'False'
        tag_nfc.save()
        return redirect('tag_nfc_list')
    else:
        return render(request, 'backend/tag_nfc_disable.html', {'tag_nfc':tag_nfc})



#Habilitar tag
@login_required(login_url='user_login')
def tag_nfc_enable(request, id):
    tag_nfc = Tag_nfc.objects.get(id = id)
    if request.method == 'POST':
        tag_nfc.available = 'True'
        tag_nfc.save()
        return redirect('tag_nfc_list')
    else:
        return render(request, 'backend/tag_nfc_enable.html', {'tag_nfc':tag_nfc})


#Editar tag
@login_required(login_url='user_login')
def tag_nfc_edit(request, id):
    tag_nfc = Tag_nfc.objects.get(id = id)
    if request.method == 'GET':
        form = Tag_nfc_Form(instance = tag_nfc)
    else:
        form = Tag_nfc_Form(request.POST, instance = tag_nfc)
        if form.is_valid():
            form.save()
        return redirect ('tag_nfc_list')
    return render(request, 'backend/tag_nfc_edit.html', {'form':form, 'tag_nfc':tag_nfc})
