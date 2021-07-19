from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListRes.as_view()),
    path('<int:pk>/', views.DetailRes.as_view()),
]