from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('login/', views.Login.as_view(),name='signin'),
    path('logout/', views.Logout.as_view(),name='logout'),
    path('confirm-logout/', views.ConfirmLogout.as_view(),name='confirm-logout'),
    path('register/', views.Register.as_view(),name='register'),
    path('token-send/', views.TokenSend.as_view(),name='token-send'),
    path('verify-account/<str:auth_token>/', views.AccountVerify.as_view(),name='verify-account'),
    path('search/', views.Search.as_view(),name='search'),
]
