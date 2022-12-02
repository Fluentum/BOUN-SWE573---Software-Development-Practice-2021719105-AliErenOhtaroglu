from django.urls import path

from . import views



urlpatterns = [

      path('', views.home, name='zenmind-home'),
      path('about/', views.about, name='zenmind-about'),
      
#path to be used in login.
#   path('accounts/login/', views.LoginView.as_view(), name='login'),

]