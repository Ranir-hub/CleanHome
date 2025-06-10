from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from order import views

app_name = 'order'

urlpatterns = [
    path('', views.order_list, name = 'order_list'),
    path('order_create/<slug:slug>', views.order_create, name = 'order_create'),
    path('order_delete/<slug:slug>', views.order_delete, name = 'order_delete'),
    path('order_update/<slug:slug>', views.order_update, name = 'order_update')
]
