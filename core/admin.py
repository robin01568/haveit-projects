from django.contrib import admin
from .models import *
from .sakib import *
# Register your models here.
admin.site.register(Sakib)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(SubDistrict)