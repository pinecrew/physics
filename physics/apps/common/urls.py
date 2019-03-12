from django.urls import path
from physics.apps.common import views
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path('', views.index, name='index'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', logout_then_login, name='logout'),
]
