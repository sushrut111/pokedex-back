from django.urls import path
from categories import views


urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('categories/<int:cid>/', views.CategoryView.as_view()),
    path('pokemon/', views.PokemonMapView.as_view()),
    path('pokemon/<int:pid>/', views.PokemonMapView.as_view()),
    

]