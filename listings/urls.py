from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.create_listing, name='create_listing'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('toggle_favorite/<int:listing_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_list, name='favorite_list'),
]