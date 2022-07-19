"""price_pal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from grocery.views import home_view, search_results_view, add_item_view, update_price_view, shopping_list_view

urlpatterns = [
    path('', home_view, name='home'),
    path('search-results/', search_results_view, name='search_results'),
    path('add-item/', add_item_view, name='add_item'),
    path('update-price/', update_price_view, name='update_price'),
    path('shopping-list/', shopping_list_view, name='shopping_list'),
    path('admin/', admin.site.urls),
]
