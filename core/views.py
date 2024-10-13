from django.shortcuts import render
from .models import *

# Create your views here.

def load_districts(request):
    division_id = request.GET.get('division_id')
    objs = District.objects.filter(division__id=division_id).order_by('name')
    return render(request, 'store/load_data/dropdown_list.html', {'objs': objs})


def load_sub_districts(request):
    district_id = request.GET.get('district_id')
    objs = SubDistrict.objects.filter(district__id=district_id).order_by('name')
    return render(request, 'store/load_data/dropdown_list.html', {'objs': objs})