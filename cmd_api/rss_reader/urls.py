from django.urls import path
from . import views

urlpatterns = [
    path('feeds/', views.feed_list),
    path('feeds/<int:pk>/', views.feed_detail),
]