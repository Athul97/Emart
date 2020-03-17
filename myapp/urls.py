from django.urls import path
from . import views

urlpatterns = [
    path('', views.fn_admin),
    path('category', views.fn_category),
    path('subcat', views.fn_subcat),
    path('brand/', views.fn_brand),
    path('product', views.fn_product),
    path('adminLog/', views.fn_adminLog),
    path('addcat/', views.fn_cat_add),
    path('addsubcat/', views.fn_subcat_add),
    path('addbrand/', views.fn_brand_add),
   
    path('home', views.fn_home),
    path('userlog/', views.fn_userlog),
    path('signin/', views.fn_signin),
    path('signin1', views.fn_signin1),

    path('userlogin/', views.fn_userLogin),
    path('usersignup/', views.fn_UserSgup),

    path('prolist', views.fn_prolist),
    path('cart', views.fn_cart)
]

