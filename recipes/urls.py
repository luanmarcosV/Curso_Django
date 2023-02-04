from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.home, name='home'), #/home/
    path('recipes/search/', views.search, name='search'), #/search
    path('recipes/<int:id>/', views.recipe, name='recipe'), #/recipe/
    path('recipes/category/<int:category_id>/', views.category, name='category'), #/category/
    
]
