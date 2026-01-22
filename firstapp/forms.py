from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Order, Category, Product, AdminUser

class OrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True  
    )

    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'address', 'status', 'products']



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class SignUpForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False, label="Register as admin")

    class Meta:
        model = AdminUser
        fields = ['username', 'email', 'password1', 'password2','admin_key']

class LoginForm(AuthenticationForm):
    class Meta:
        model = AdminUser
        fields = ['username', 'password']



    