from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('website/<str:pk>/', views.website, name="website"),
    path('create-catalog/', views.createCatalog, name="create-catalog"),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.website_list_by_category, name='website_list_by_category'),
    path('websites/edit/<int:website_id>/', views.edit_website, name='edit_website'),
    path('websites/delete/<int:website_id>/', views.delete_website, name='delete_website'),
]