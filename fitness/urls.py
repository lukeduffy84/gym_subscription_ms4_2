from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
import store.views as store_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("staff/", include("staff.urls")),
    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("", include("store.urls"))
]
