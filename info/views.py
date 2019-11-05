from django.shortcuts import render, redirect
from django import forms
from .forms import InfoForm
from login.forms import UserForm
from . import models


def info(request):
    if request.session.get('is_login', None) is None:
        return render(request, 'info/info.html', locals())
    else:
        user_id = request.session.get('user_id')
        user = models.User.objects.get(pk=user_id)
        message = "请检查填写的内容！"
        if request.method == "POST":
            info_form = InfoForm(request.POST)
            if info_form.is_valid():
                user.username = info_form.cleaned_data['username']
                user.password = info_form.cleaned_data['password']
                user.province = info_form.cleaned_data['province']
                user.sex = info_form.cleaned_data['sex']
                user.subject = info_form.cleaned_data['subject']
                user.score = info_form.cleaned_data['score']

                # 观察用户名是否存在
                if (not models.User.objects.filter(username=user.username)) or \
                        (user.username == request.session['user_name']):
                    user.save()
                    message = '提交成功'
                    request.session['user_name'] = user.username

                else:
                    message = '用户名已存在，请更换用户名'

        info_form = InfoForm(initial={'username': user.username,
                                      'password': user.password,
                                      'sex': user.sex,
                                      'province': user.province,
                                      'subject': user.subject,
                                      'score': user.score,
                                      })

        return render(request, 'info/info.html', locals())
