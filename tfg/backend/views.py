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


from .models import Publicity_campaign, UserProfile, Product, Product_history, Recipe, Tag_nfc, Register_activity, Point
from django.db.models import Count

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
    point = Point.objects.count()
    tags_touch = Register_activity.objects.filter(activity_name='TAG NFC').count()
    promotion_accept = Register_activity.objects.filter(activity_name='Promocion', tag_nfc_status='Correcto').count()
    promotion_denied = Register_activity.objects.filter(activity_name='Promocion', tag_nfc_status='Denegado. Promoción ya registrada').count()
    datetime1 = datetime.now()
    campaign_enable = Publicity_campaign.objects.filter(date_end__gte = datetime1).count()
    campaign_disable = Publicity_campaign.objects.filter(date_end__lt = datetime1).count()
    datos = Register_activity.objects.values('date').order_by('date').annotate(count=Count('date'))[:10] #IMPORTANTE, HAY QUE ELIMINAR PARA QUE SALGAN LOS 5 ÚLTIMOS DÍAS
    nfc_date = Register_activity.objects.values('date').filter(activity_name='TAG NFC').order_by('activity_name').annotate(count=Count('date'))[:10]

    return render(request, 'backend/index.html',{'users':users, 'nfc_date':nfc_date, 'datos':datos, 'campaign_disable':campaign_disable, 'campaign_enable':campaign_enable, 'promotion_accept':promotion_accept, 'promotion_denied':promotion_denied, 'campaign':campaign, 'products':products, 'recipes': recipes, 'users_admin':users_admin, 'tags':tags, 'tags_touch':tags_touch, 'point': point})

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
                    print ("HOLA")
                    return redirect('index')
                
            
        else:
            print ("adios")
            error = True
            return render(request, 'backend/login.html', {'form': form, 'error':error})

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
########################## NFC_TAG METHODS ####################################################
###############################################################################################


#Crear tag
@login_required(login_url='user_login')
def tag_nfc_create(request):
    if request.method == 'POST':
        form = Tag_nfc_Form(request.POST)
        if form.is_valid():
            form.instance.user = request.user.username
            form.save()
            return redirect('tag_nfc_list')
    else:
        form = Tag_nfc_Form()
        return render(request, 'backend/tag_nfc_create.html', {'form':form,})

#Ver tag
@login_required(login_url='user_login')
def tag_nfc(request, id):
    tag_nfc = Tag_nfc.objects.get(id = id)
    return render(request, 'backend/tag_nfc.html', {'tag_nfc':tag_nfc})



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
            form.instance.user = request.user.username
            form.instance.date = datetime.now()
            form.save()
        return redirect ('tag_nfc_list')
    return render(request, 'backend/tag_nfc_edit.html', {'form':form, 'tag_nfc':tag_nfc})

from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage

###########################################################
########################ACTIVITY###########################
###########################################################

#Ver tag
@login_required(login_url='user_login')
def register_activity_list(request):
    register_activity = Register_activity.objects.all().order_by('id').reverse()
    paginator = Paginator(register_activity, 6)
    num_index = Register_activity.objects.filter(activity_name='INDEX').count()
    num_inicio = Register_activity.objects.filter(activity_name='Inicio').count()
    num_cierre = Register_activity.objects.filter(activity_name='Cierre').count()
    num_list_camp = Register_activity.objects.filter(activity_name='Lista de campañas').count()
    num_list_product = Register_activity.objects.filter(activity_name='Lista de productos').count()
    num_list_recipe = Register_activity.objects.filter(activity_name='Lista de recetas').count()
    register = Register_activity.objects.filter(activity_name='Registro').count()
    num_camp = Register_activity.objects.filter(activity_name='Campaña de publicidad').count()
    puntos = Register_activity.objects.filter(activity_name='Lista de puntos').count()
    product = Register_activity.objects.filter(activity_name='Producto').count()
    recipe = Register_activity.objects.filter(activity_name='Receta').count()
    tag = Register_activity.objects.filter(activity_name='TAG NFC').count()
    promotion = Register_activity.objects.filter(activity_name='Promocion').count()


    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        register_activity = paginator.page(page)
    except (InvalidPage, EmptyPage):
        register_activity = paginator.page(paginator.num_pages)
    return render(request, 'backend/register_activity_list.html', {'register_activity':register_activity, 'promotion':promotion, 'tag':tag, 'recipe':recipe, 'product':product, 'puntos':puntos, 'num_camp':num_camp, 'register':register,'num_list_recipe':num_list_recipe,'num_list_product':num_list_product, 'num_list_camp':num_list_camp, 'num_index':num_index, 'num_inicio':num_inicio, 'num_cierre':num_cierre})


from django.db.models import Q



@login_required(login_url='user_login')
def register_activity_sesions(request):    
    register_activity = Register_activity.objects.filter(Q(activity = "Sesión") |Q(activity = "Visita sección", activity_name="Registro") ).order_by('id').reverse()
    paginator = Paginator(register_activity, 6)
    register_activity_data = Register_activity.objects.values('activity_name','date').filter(Q(activity = "Sesión") |Q(activity = "Visita sección", activity_name="Registro")).order_by('date').annotate(count=Count('date'))
    register_activity_inicio = Register_activity.objects.values('activity_name','date').filter(activity = "Sesión", activity_name="Inicio").order_by('date').annotate(count=Count('date'))
    register_activity_cierre = Register_activity.objects.values('activity_name','date').filter(activity = "Sesión", activity_name="Cierre").order_by('date').annotate(count=Count('date'))
    register_activity_register = Register_activity.objects.values('activity_name','date').filter(Q(activity = "Visita sección", activity_name="Registro")).order_by('date').annotate(count=Count('date'))
    register_activity_register_count = Register_activity.objects.filter(activity = "Visita sección", activity_name="Registro", user__isnull=True).count()
    register_activity_register_count_register = Register_activity.objects.filter(activity = "Visita sección", activity_name="Registro", user__isnull=False).count()

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        register_activity = paginator.page(page)
    except (InvalidPage, EmptyPage):
        register_activity = paginator.page(paginator.num_pages) 
    return render(request, 'backend/register_activity_sesions.html', {'register_activity_register_count_register':register_activity_register_count_register, 'register_activity_register_count':register_activity_register_count, 'register_activity_register':register_activity_register, 'register_activity_cierre':register_activity_cierre, 'register_activity_inicio':register_activity_inicio, 'register_activity':register_activity, 'register_activity_data':register_activity_data})


@login_required(login_url='user_login')
def register_activity_campaign(request, id):
    if id == "0":    
        register_activity = Register_activity.objects.filter(Q(activity = "Visita sección", activity_name= "Lista de campañas") | Q(activity = "Visita sección", activity_name= "Campaña de publicidad")).order_by('id').reverse()
    if id == "1":    
        register_activity = Register_activity.objects.filter(activity = "Visita sección", activity_name= "Lista de campañas").order_by('id').reverse()
    if id == "2":    
        register_activity = Register_activity.objects.filter(activity = "Visita sección", activity_name= "Campaña de publicidad").order_by('id').reverse()
    
    register_activity_listcampaign_count = Register_activity.objects.values('date').filter(Q(activity = "Visita sección", activity_name="Lista de campañas")).order_by('date').annotate(count=Count('date'))
    register_activity_campaign_count = Register_activity.objects.values('date').filter(Q(activity = "Visita sección", activity_name="Campaña de publicidad")).order_by('date').annotate(count=Count('date'))

       
    paginator = Paginator(register_activity, 6)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        register_activity = paginator.page(page)
    except (InvalidPage, EmptyPage):
        register_activity = paginator.page(paginator.num_pages) 
    return render(request, 'backend/register_activity_campaing.html', {'id':id, 'register_activity_listcampaign_count':register_activity_listcampaign_count, 'register_activity':register_activity, 'register_activity_campaign_count':register_activity_campaign_count })

@login_required(login_url='user_login')
def register_activity_product(request, id):
    if id == "0":    
        register_activity = Register_activity.objects.filter(Q(activity = "Visita sección", activity_name= "Lista de productos") | Q(activity = "Visita sección", activity_name= "Producto")).order_by('id').reverse()
    if id == "1":    
        register_activity = Register_activity.objects.filter(activity = "Visita sección", activity_name= "Lista de productos").order_by('id').reverse()
    if id == "2":    
        register_activity = Register_activity.objects.filter(activity = "Visita sección", activity_name= "Producto").order_by('id').reverse()
    
    register_activity_listproduct_count = Register_activity.objects.values('date').filter(Q(activity = "Visita sección", activity_name="Lista de productos")).order_by('date').annotate(count=Count('date'))
    register_activity_product_count = Register_activity.objects.values('date').filter(Q(activity = "Visita sección", activity_name="Producto")).order_by('date').annotate(count=Count('date'))

       
    paginator = Paginator(register_activity, 6)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        register_activity = paginator.page(page)
    except (InvalidPage, EmptyPage):
        register_activity = paginator.page(paginator.num_pages) 
    return render(request, 'backend/register_activity_product.html', {'id':id, 'register_activity_listproduct_count':register_activity_listproduct_count, 'register_activity':register_activity, 'register_activity_product_count':register_activity_product_count })


@login_required(login_url='user_login')
def register_activity_recipe(request, id):
    if id == "0":    
        register_activity = Register_activity.objects.filter(Q(activity = "Visita sección", activity_name= "Lista de recetas") | Q(activity = "Visita sección", activity_name= "Receta")).order_by('id').reverse()
    if id == "1":    
        register_activity = Register_activity.objects.filter(activity = "Visita sección", activity_name= "Lista de recetas").order_by('id').reverse()
    if id == "2":    
        register_activity = Register_activity.objects.filter(activity = "Visita sección", activity_name= "Receta").order_by('id').reverse()
    
    register_activity_listrecipe_count = Register_activity.objects.values('date').filter(Q(activity = "Visita sección", activity_name="Lista de recetas")).order_by('date').annotate(count=Count('date'))
    register_activity_recipe_count = Register_activity.objects.values('date').filter(Q(activity = "Visita sección", activity_name="Receta")).order_by('date').annotate(count=Count('date'))

       
    paginator = Paginator(register_activity, 6)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        register_activity = paginator.page(page)
    except (InvalidPage, EmptyPage):
        register_activity = paginator.page(paginator.num_pages) 
    return render(request, 'backend/register_activity_recipe.html', {'id':id, 'register_activity_listrecipe_count':register_activity_listrecipe_count, 'register_activity':register_activity, 'register_activity_recipe_count':register_activity_recipe_count })


@login_required(login_url='user_login')
def register_activity_nfc(request):
    register_activity = Register_activity.objects.filter(activity="Visita sección", activity_name="TAG NFC").order_by('id').reverse()

    register_activity_no_register = Register_activity.objects.filter(activity="Visita sección", activity_name="TAG NFC", user__isnull=True).count()
    register_activity_register = Register_activity.objects.filter(activity="Visita sección", activity_name="TAG NFC", user__isnull=False).count()

    register_activity_nfc_count = Register_activity.objects.values('date').filter(Q(activity = "Visita sección", activity_name="TAG NFC")).order_by('-date').annotate(count=Count('date'))[:4]

       
    paginator = Paginator(register_activity, 6)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        register_activity = paginator.page(page)
    except (InvalidPage, EmptyPage):
        register_activity = paginator.page(paginator.num_pages) 
    return render(request, 'backend/register_activity_nfc.html', {'register_activity_nfc_count':register_activity_nfc_count, 'register_activity':register_activity, 'register_activity_register':register_activity_register, 'register_activity_no_register':register_activity_no_register })




@login_required(login_url='user_login')
def register_activity_map(request, id):
    register_activity = Register_activity.objects.get(id=id)    
    return render(request, 'backend/register_activity_map.html', {'register_activity':register_activity})


@login_required(login_url='user_login')
def register_activity_promotion(request):
    register_activity = Register_activity.objects.filter(activity="Registro", activity_name="Promocion").order_by('id').reverse()

    register_activity_promo = Register_activity.objects.filter(activity="Registro", activity_name="Promocion", tag_nfc_status="Correcto").count()
    register_activity_no_promo = Register_activity.objects.filter(activity="Registro", activity_name="Promocion", tag_nfc_status="Denegado. Promoción ya registrada").count()

    register_activity_promo_count = Register_activity.objects.values('date').filter(activity="Registro", activity_name="Promocion", tag_nfc_status="Correcto").order_by('-date').annotate(count=Count('date'))
    register_activity_no_promo_count = Register_activity.objects.values('date').filter(activity="Registro", activity_name="Promocion", tag_nfc_status="Denegado. Promoción ya registrada").order_by('-date').annotate(count=Count('date'))
   
    paginator = Paginator(register_activity, 6)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        register_activity = paginator.page(page)
    except (InvalidPage, EmptyPage):
        register_activity = paginator.page(paginator.num_pages) 
    return render(request, 'backend/register_activity_promotion.html', {'register_activity_no_promo_count':register_activity_no_promo_count,'register_activity_promo_count':register_activity_promo_count,'register_activity':register_activity, 'register_activity_promo':register_activity_promo, 'register_activity_no_promo':register_activity_no_promo })

