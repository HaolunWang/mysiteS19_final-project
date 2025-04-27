"""mysiteS19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from myapp import views

APPEND_SLASH = True

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),

    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^$', views.indexView.as_view(), name='index'),
    # re_path(r'^$', views.index, name='index'),

    path('myapp/about', views.about, name='about'),
    re_path(r'^myapp/(?P<cat_no>\d+)', views.detail, name='detail'),
    # re_path(r'^myapp/(?P<cat_no>\d+)', views.detail.as_view(), name='detail'),

    path('myapp/products', views.products, name='product'),
    path('myapp/place_order', views.place_order, name='place_order'),
    re_path(r'^myapp/products/(?P<prod_id>\d+)', views.productdetail, name='productdetail'),
    # re_path(r'^myapp/products/(?P<prod_id>\d+)', views.productdetailView.as_view(), name='productdetail'),

    path('myapp/order_response', views.place_order, name='order_response'),
    re_path(r'^myorder/$', views.myorder, name='myorder'),
]




