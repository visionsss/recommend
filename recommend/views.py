from django.shortcuts import render
from . import models
from login.models import User
import pandas as pd
from django.core import serializers


def re_school(request):
    try:
        score = User.objects.filter(username=request.session['user_name'])[0].score
        print(score)
        school = models.re_school.objects.filter(score_low__range=(score - 30, score + 30))
        print(school)
    except:
        pass
    return render(request, 'recommend/re_school.html', locals())


def re_profession(request):
    message = models.Profession.objects.values_list()
    message = pd.DataFrame(message)
    type1 = message.iloc[:, 1].unique()
    pro_js = serializers.serialize("json", models.Profession.objects.all())

    return render(request, 'recommend/re_profession.html', locals())
