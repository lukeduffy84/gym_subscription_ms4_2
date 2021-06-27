from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('login',customer_login,name='login'),
    path('register',customer_signup,name='register'),
    path('addproduct',add_product,name='addproduct'),
    path('editproduct/<int:pid>',edit_product,name='editproduct'),
    path('delete/<int:pid>',delete_product,name='delete'),
    path('product/<int:pid>',view_single_product,name='product'),
    path('viewproduct/<int:pid>',view_my_product,name='viewproduct'),
    path('myproduct',my_products,name='myproduct'),
    path('allprogram/<str:view_by>',all_program,name='fitness'),
    path('merchandise',merchandise,name='merchandise'),
    path('programs',online_programs,name='programs'),
    path('supplements',supplements,name='supplements'),
    path('shopping',shopping_bag,name='shopping'),
    path('blogs',blogs,name='blogs'),
    path('testimonials',testimonials,name='testimonials'),
    path('checkout',checkout,name='checkout'),

]
