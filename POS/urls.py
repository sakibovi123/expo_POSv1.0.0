"""POS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from posApp import views
from posApp.views import *
from django.conf import settings
from django.conf.urls.static import static
from posApp.api import api_add_to_cart, api_remove_from_cart, api_checkout



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_home_page, name="base"),
    
    # Login
    path('login/', views.admin_login, name="admin_login"),
    path('logout/', views.admin_logout, name="admin_logout"),
    
    # Employee Details Path
    
    path('details/<int:id>', views.get_emp_details, name="get_emp_details"),

    # Products page URL

    path('all_products/', views.get_products_page, name="get_products_page"),
    
    # Category URLS

    path('categories/', views.get_category_page, name="get_category_page"),

    ## Brands URLS

    path('brands/', views.get_brand, name="get_brand"),

    ## Sell page

    path('get_sell_page/', views.get_sell_page, name="get_sell_page"),


    ### API REQUESTS ###

    path('api/api_add_to_cart/', api_add_to_cart, name="api_add_to_cart"),
    path('api/api_remove_from_cart/', api_remove_from_cart, name="api_remove_from_cart"),
    path('api/api_checkout/', api_checkout, name="api_checkout"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
