# thrifty/listings/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.create_listing, name='create_listing'), 
    path('favorite/<int:listing_id>/', views.favorite_listing, name='favorite_listing'),
    path('favorites/', views.favorite_list, name='favorite_list'),
     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
     
]