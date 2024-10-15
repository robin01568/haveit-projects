from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import *
from core.models import *
from Store.models import *
from PaymentApp.models import *
from UserAccount.models import *


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/index.html')


## ============================= Location data Start ===========================
## ============= Division =============
def division_list(request):
    query = Division.objects.all()
    return render(request, 'dashboard/location-data/division/list.html', {'query': query})

def division_add(request):
    if request.method == 'POST':
        form = DivisionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('division_list')
    else:
        form = DivisionForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

def division_edit(request, id):
    obj = Division.objects.get(id=id)
    if request.method == 'POST':
        form = DivisionForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('division_list')
    else:
        form = DivisionForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

def division_delete(request, id):
    Division.objects.get(id=id).delete()
    return redirect('division_list')

## ============= District ==============

## ============= Sub District ==========

## ============================= Location data End =============================
## ============================= Web data Start =============================
## ============= Website information ==============

## ============= Terms & Condition ==============

def terms_conditions_list(request):
    obj_list = TermsCondition.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/web-data/terms/list.html', {'query': query})

def terms_conditions_add(request):
    if request.method == 'POST':
        form = TermsConditionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('terms_conditions_list')
    else:
        form = TermsConditionForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

def terms_conditions_edit(request, id):
    obj = TermsCondition.objects.get(id=id)
    if request.method == 'POST':
        form = TermsConditionForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('terms_conditions_list')
    else:
        form = TermsConditionForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

def terms_conditions_delete(request, id):
    TermsCondition.objects.get(id=id).delete()
    return redirect('terms_conditions_list')

## ============================= Web data End =============================