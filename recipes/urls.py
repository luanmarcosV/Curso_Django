from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"), #/home/
    path(
        'recipes/search/',
        views.RecipeListViewSearch.as_view(), name="search"
    ),
    path(
        'recipes/category/<int:category_id>/',
        views.RecipeListViewCategory.as_view(), name="category"
    ),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe"), #/recipe/
    path(
        'recipes/theory/',
        views.theory,
        name='theory',
    ),
    
]
