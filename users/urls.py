from django.urls import path
from django.contrib.auth.views import LoginView

from .views import LogOutView,LandingView, dashboard_view, user_register, user_login

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('login/', user_login, name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='user_profile'),
    path('signup/', user_register, name='user_register'),
]



