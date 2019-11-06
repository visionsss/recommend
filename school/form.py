from django import forms
from . import models
from django.db.models import Count


class school_form(forms.Form):
    school_name = forms.CharField(label="院校名称")
    city = forms.CharField(label="城市")




