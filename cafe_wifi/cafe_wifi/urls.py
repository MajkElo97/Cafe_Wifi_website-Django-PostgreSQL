"""cafe_wifi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cafes.views import home, CafeListView, CafeCreateView, get_random_cafe, get_all_cafe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cafes/', CafeListView.as_view(), name='cafe-list'),
    path('add/', CafeCreateView.as_view(), name='cafe-create'),
    path('api/random/', get_random_cafe, name='api-cafe-random'),
    path('api/all_cafes/', get_all_cafe, name='api-cafe-all'),
]