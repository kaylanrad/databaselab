from django.contrib import admin
from django.urls import path
from Api import views

urlpatterns = [
    path('ShowAllBooksView/', views.ShowAllBooksView.as_view()),
]
