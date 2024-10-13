from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),

    ## ==================== Divisions =================
    path('division-list/', division_list, name="division_list"),
    path('division-add/', division_add, name="division_add"),
    path('division-edit/<int:id>', division_edit, name="division_edit"),
    path('division-delete/<int:id>', division_delete, name="division_delete"),

    ## ==================== Terms conditions =================
    path('terms-conditions-list/', terms_conditions_list, name="terms_conditions_list"),
    path('terms-conditions-add/', terms_conditions_add, name="terms_conditions_add"),
    path('terms-conditions-edit/<int:id>', terms_conditions_edit, name="terms_conditions_edit"),
    path('terms-conditions-delete/<int:id>', terms_conditions_delete, name="terms_conditions_delete"),
]