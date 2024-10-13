from django.urls import path
from .views import *

urlpatterns = [
    path('load-districts/', load_districts, name="load_districts"),
    path('load-sub-districts/', load_sub_districts, name="load_sub_districts"),
]