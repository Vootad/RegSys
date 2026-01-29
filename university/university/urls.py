
from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.shortcuts import redirect
# اضافه کردن این خط:
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
]
