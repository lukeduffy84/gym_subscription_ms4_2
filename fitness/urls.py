from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
import store.views as store_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("staff/", include("staff.urls")),
    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("register/<str:next>/", store_views.register, name="register"),
    path("tag_router/<str:tag>/", store_views.tag_router, name="tag_router"),
    path("", store_views.home, name="home"),
    path("fitness/<str:view_by>/", store_views.fitness, name="fitness"),
    path("supplements", store_views.supplements, name="supplements"),
    path("all_products", store_views.all_products, name="all_products"),
    path("merchandise", store_views.merchandise, name="merchandise"),
    path("online_coaching", store_views.online_coaching, name="online_coaching"),
    path("product/<int:id>/", store_views.product_detail, name="product"),
    path("testimonials", store_views.testimonials, name="testimonials"),
    path("cart", store_views.cart, name="cart"),
    path("add_to_cart", store_views.add_to_cart, name="add_to_cart"),
    path("update_cart_item", store_views.update_cart_item, name="update_cart_item"),
    path("remove_cart_item/<int:id>/", store_views.remove_cart_item, name="remove_cart_item"),
    path("checkout", store_views.checkout, name="checkout"),
    path("clear", store_views.clear_session, name="clear"),
]