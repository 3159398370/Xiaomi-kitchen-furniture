from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('about/', views.about, name='about'),
    path('category_nav/', views.category_nav, name='category_nav'),
    path('kitchen_furniture/', views.kitchen_furniture, name='kitchen_furniture'),
    path('installation/', views.installation, name='installation'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('delete-account/', views.delete_account, name='delete_account'),
]