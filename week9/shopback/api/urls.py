from django.urls import path

from api import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('categories/', views.categories),
    path('categories/<int:id>/', views.category_detailed),
    path('categories/<int:id>/products/', views.category_product),
   
]