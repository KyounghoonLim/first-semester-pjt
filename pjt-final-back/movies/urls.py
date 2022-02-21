from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
    path('detail/<int:movie_pk>/', views.detail),
    path("genres/", views.get_genres),
    path('review/<int:movie_pk>/', views.review),
    path('review/<int:movie_pk>/<int:review_pk>/', views.review_detail),

]
