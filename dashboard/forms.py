from django import forms
from core.models import *
from Store.models import *
from PaymentApp.models import *
from UserAccount.models import *
from ckeditor.widgets import CKEditorWidget

from ckeditor_uploader.widgets import CKEditorUploadingWidget
## ============================= Location data Start ===========================
## ============= Division ==============
class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = "__all__"

## ============= Division ==============
# class TermsConditionForm(forms.ModelForm):
#     class Meta:
#         model = TermsCondition
#         fields = "__all__"



class TermsConditionForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = TermsCondition
        fields = '__all__'

# class TermsConditionAdmin(admin.ModelAdmin):
#     form = TermsConditionForm

# admin.site.register(TermsCondition, TermsConditionForm)
