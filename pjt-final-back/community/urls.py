from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.community),
    path('<int:community_pk>/', views.community_detail),
    path('<int:community_pk>/like/', views.community_like),
    path('<int:community_pk>/comment/', views.comment),
    path('<int:community_pk>/comment/<int:comment_pk>/', views.comment_detail),
    path('<int:community_pk>/comment/<int:comment_pk>/like/', views.comment_like),
]
