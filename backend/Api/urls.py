from django.contrib import admin
from django.urls import path
from Api import views
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.SignUp.as_view()),

    path('ShowAllBooks/', views.ShowAllBooksView.as_view()),
    path('ShowSingleBook/', views.ShowSingleBook.as_view()),
    path('ShowAllGenre/', views.ShowAllGenre.as_view()),
    path('ShowSingleGenre/', views.ShowSingleGenre.as_view()),
    path('ShowAllAuthor/', views.ShowAllAuthor.as_view()),
    path('ShowSingleAuthor/', views.ShowSingleAuthor.as_view()),
    path('AddToShopcard/', views.AddToShopcard.as_view()),
    path('RemoveFromShopcard/', views.RemoveFromShopcard.as_view()),
    path('ShowShopcard/', views.ShowShopcard.as_view()),
    path('CreateFactor/', views.CreateFactor.as_view()),
    path('PayFactor/', views.PayFactor.as_view()),
       
]
