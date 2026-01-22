from django.shortcuts import render, redirect, get_object_or_404
from .models import Order,  Category, AdminUser,Product
from .forms import OrderForm, CategoryForm, AdminUserForm, ProductForm,SignUpForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
import logging



def about(request):
    return render(request,"html/about.html")

def blog(request):
    return render(request,"html/blog.html")

def blogSingle(request):
    return render(request,"html/blogSingle.html")

def contact(request):
    return render(request,"html/contact.html")

def index(request):
    return render(request,"html/index.html")

def menu(request):
    products = Product.objects.all() 
    return render(request, 'html/menu.html', {'products': products})

def services(request):
    return render(request,"html/services.html")


# Dashboard main pages
def indexDash(request):
    return render(request, 'dashboard/indexDash.html')

def add_product(request):
    return render(request, 'dashboard/add_product.html')

def edit_product(request):
    return render(request, 'dashboard/edit_product.html')

def delete_product(request):
    return render(request, 'dashboard/Delete_product.html')

def list_product(request):
    return render(request, 'dashboard/list_Product.html')

def profile(request):
    return render(request, 'dashboard/profile.html')

def base(request):
    return render(request, 'dashboard/base.html')

def footerDash(request):
    return render(request, 'dashboard/footerDash.html')

def navDash(request):
    return render(request, 'dashboard/navDash.html')

def sideDash(request):
    return render(request, 'dashboard/sideDash.html')

def charts(request):
    return render(request, 'dashboard/charts.html')

def maps_google(request):
    return render(request, 'dashboard/maps_google.html')

def icons_feather(request):
    return render(request, 'dashboard/icons_feather.html')

#order

# list order
def list_order(request):
    orders = Order.objects.all()
    return render(request, 'dashboard/list_order.html', {'orders': orders})

# update order 
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تعديل الطلب بنجاح!")
            return redirect('list_order')
    else:
        form = OrderForm(instance=order)
    return render(request, 'dashboard/create_order.html', {'form': form})

# Delete order
def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return redirect('list_order')


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "تم إضافة الطلب بنجاح!") 
            return redirect('list_order')
        else:
            messages.error(request, "هناك خطأ، الرجاء التحقق من البيانات.")
    else:
        form = OrderForm()
    return render(request, 'dashboard/create_order.html', {'form': form})


#category

# List  categories
def list_category(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/list_category.html', {'categories': categories})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إضافة القسم بنجاح!") 
            return redirect('list_category')
        else:
            messages.error(request, "هناك خطأ، الرجاء التحقق من البيانات.")
    else:
        form = CategoryForm()
    return render(request, 'dashboard/create_category.html', {'form': form})


def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تعديل القسم بنجاح!")
            return redirect('list_category')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/create_category.html', {'form': form})


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('list_category')

#Product 
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إضافة المنتج بنجاح!") 
            return redirect('list_product')
        else:
            messages.error(request, "هناك خطأ، الرجاء التحقق من البيانات.")
    else:
        form = ProductForm()

    return render(request, 'dashboard/create_product.html', {'form': form})

def list_product(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'dashboard/list_product.html', {'products': products})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تعديل المنتج بنجاح!")
            return redirect('list_product')
    else:
        form = ProductForm(instance=product)

    return render(request, 'dashboard/create_product.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('list_product')


#adminuser

# صفحة إضافة 
def add_admin_user(request):
    if request.method == "POST":
        form = AdminUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إضافة المستخدم بنجاح!")
        else:
            messages.error(request, "هناك خطأ، الرجاء التحقق من البيانات.")
            return redirect('admin_user_list')
    else:
        form = AdminUserForm()
    return render(request, 'dashboard/add_admin_user.html', {'form': form})

# صفحة قائمة 
def admin_user_list(request):
    users = AdminUser.objects.all()
    return render(request, 'dashboard/admin_user_list.html', {'users': users})

# حذف 
def delete_admin_user(request, pk):
    user = get_object_or_404(AdminUser, pk=pk)
    user.delete()
    return redirect('admin_user_list')

# تعديل 
def update_admin_user(request, pk):
    user = get_object_or_404(AdminUser, pk=pk)
    if request.method == "POST":
        form = AdminUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تعديل المستخدم بنجاح!")
            return redirect('admin_user_list')
    else:
        form = AdminUserForm(instance=user)
    return render(request, 'dashboard/add_admin_user.html', {'form': form})

# Signup
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            
            admin_key = form.cleaned_data.get('admin_key')
            if admin_key == 'sec123': 
                user.is_admin = True
            else:
                user.is_admin = False
            
            user.save()
            login(request, user)  
            
            
            if user.is_admin:
                return redirect('indexDash')  
            else:
                return redirect('login')  
    else:
        form = SignUpForm()
    return render(request, 'html/signup.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)  # فقط المسؤول يمكنه الدخول
def dashboard(request):
    
    return render(request, 'dashboard/indexDash.html')







logger = logging.getLogger('django.security')
def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('menu')  

        else:
           
            logger.warning(f"Failed login attempt for email: {email}")
            error = "Invalid credentials"
            return render(request, 'html/login.html', {'error': error})

   
    return render(request, 'html/login.html')





def logout_view(request):
    logout(request) 
    messages.success(request, "You have logged out successfully!")  
    return redirect('login') 


@login_required
def add_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    
    order = Order.objects.create(
        customer_name=request.user.username,
        phone="None",  
        address="None"
    )
    order.products.add(product)
    order.save()

    return redirect('menu')


    