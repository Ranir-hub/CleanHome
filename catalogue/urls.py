from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from catalogue import views

app_name = 'catalogue'

urlpatterns = [
    path('', views.catalogue, name = 'list'),
    path('item_create/', views.item_create, name = 'item_create'),
    path('category_create/', views.category_create, name = 'category_create'),
    path('category/', views.category, name = 'category'),
    path('category/<slug:slug>', views.category_this, name = 'category_this'),
    path('category_update/<slug:slug>/', views.category_update, name = 'category_update'),
    path('category_delete/<slug:slug>/', views.category_delete, name = 'category_delete'),
    path('<slug:slug>/', views.item, name = 'item'),
    path('item_update/<slug:slug>/', views.item_update, name = 'item_update'),
    path('item_delete/<slug:slug>/', views.item_delete, name = 'item_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
