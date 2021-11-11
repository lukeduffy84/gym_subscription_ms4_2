from django.urls import path
import staff.views as staff_views

urlpatterns = [
    path('', staff_views.dashboard, name='dashboard'),
    path('orders', staff_views.orders, name='orders'),
    path('products', staff_views.product_list, name='product_list'),
    path('add_product', staff_views.add_product, name='add_product'),
    path('edit_product/<int:pid>', staff_views.edit_product, name='edit_product'),
    path('delete_product/<int:pid>', staff_views.delete_product, name='delete_product'),
]