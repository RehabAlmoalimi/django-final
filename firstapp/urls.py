from django.urls import path
from . import views

urlpatterns = [
    # Main website pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blogSingle/', views.blogSingle, name='blogSingle'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path('services/', views.services, name='services'),

    #login/signup/logout
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   

    # Dashboard main page
    path('dashboard/indexDash/', views.indexDash, name='indexDash'),

    # Dashboard pages
    path('dashboard/add_product/', views.add_product, name='add_product'),
    path('dashboard/edit_product/', views.edit_product, name='edit_product'),
    path('dashboard/delete_product/', views.delete_product, name='delete_product'),
    path('dashboard/list_product.html/', views.list_product, name='list_product'),
    path('dashboard/profile/', views.profile, name='profile'),

    # Components
    path('dashboard/base/', views.base, name='base'),
    path('dashboard/footerDash/', views.footerDash, name='footerDash'),
    path('dashboard/navDash/', views.navDash, name='navDash'),
    path('dashboard/sideDash/', views.sideDash, name='sideDash'),

    # Charts / Maps / Icons
    path('dashboard/charts/', views.charts, name='charts'),
    path('dashboard/maps_google/', views.maps_google, name='maps_google'),
    path('dashboard/icons_feather/', views.icons_feather, name='icons_feather'),


    path('dashboard/list_order/', views.list_order, name='list_order'),
    path('dashboard/create_order/', views.create_order, name='create_order'),
    path('dashboard/update_order/<int:order_id>/', views.update_order, name='update_order'),
    path('dashboard/delete_order/<int:id>/', views.delete_order, name='delete_order'),
    path('dashboard/list_category/', views.list_category, name='list_category'),
    path('dashboard/create_category/', views.create_category, name='create_category'),
    path('dashboard/update_category/<int:pk>/', views.update_category, name='update_category'),
    path('dashboard/delete_category/<int:pk>/', views.delete_category, name='delete_category'),

    path('dashboard/list_product/', views.list_product, name='list_product'),
    path('dashboard/create_product/', views.create_product, name='create_product'),
    path('dashboard/update_product/<int:pk>/', views.update_product, name='update_product'),
    path('dashboard/delete_product/<int:pk>/', views.delete_product, name='delete_product'),


    path('dashboard/admin_user_list/', views.admin_user_list, name='admin_user_list'),
    path('dashboard/add_admin_user/', views.add_admin_user, name='add_admin_user'),
    path('dashboard/update_admin_user/<int:pk>/', views.update_admin_user, name='update_admin_user'),
    path('dashboard/delete_admin_user/<int:pk>/', views.delete_admin_user, name='delete_admin_user'),

    path('add-order/<int:product_id>/', views.add_order, name='add_order')
   
]



   