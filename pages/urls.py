from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('pages/create/', views.PageCreate, name='pagecreate'),
]