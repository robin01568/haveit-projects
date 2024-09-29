from django import forms
from .models import *

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'massage', 'phone']

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'message']