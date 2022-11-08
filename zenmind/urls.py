from django.urls import path

from . import views



urlpatterns = [

      path('', views.index, name='index'),


#path to be used in login.
#   path('accounts/login/', views.LoginView.as_view(), name='login'),

]