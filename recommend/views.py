from django.shortcuts import render
from . import models
import pandas as pd
from django.core import serializers


def re_school(request):
    return render(request, 'recommend/re_school.html', locals())


def re_profession(request):
    message = models.Profession.objects.values_list()
    message = pd.DataFrame(message)
    type1 = message.iloc[:, 1].unique()
    pro_js = serializers.serialize("json", models.Profession.objects.all())

    return render(request, 'recommend/re_profession.html', locals())
