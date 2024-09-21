from django.urls import path
from .views import *

urlpatterns = [
        path('register/', register, name="register"),
        path('login/', login_view, name="login"),
        path('logout/', logout_view, name="logout"),

        path('profile-dashboard/', profile_dashboard, name="profile_dashboard"),
        path('profile/', profile, name="profile"),
        path('change-password/', change_password, name="change_password"),
]