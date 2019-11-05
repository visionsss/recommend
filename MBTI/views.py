from django.shortcuts import render, redirect

from MBTI.models import MBTIType
from . import forms
from . import models


def get_mbti_type(l):
    result = ''
    if l.count('E') > l.count('I'):
        result = result + 'E'
    else:
        result = result + 'I'
    if l.count('S') > l.count('N'):
        result = result + 'S'
    else:
        result = result + 'N'
    if l.count('T') > l.count('F'):
        result = result + 'T'
    else:
        result = result + 'F'
    if l.count('J') > l.count('P'):
        result = result + 'J'
    else:
        result = result + 'P'
    return result


def mbti(request):
    # 已登录
    if request.session.get('is_login', None) is None:
        return render(request, 'MBTI/mbti.html', locals())
    # 已完成测试，获取人格类型结果
    if request.session['is_mbti']:
        mbti_info = models.MBTIType.objects.get(mbti_type=request.session['user_mbti'])
        analysis = mbti_info.mbti_analysis
    return render(request, 'MBTI/mbti.html', locals())


def mbti_test(request):

    message = '请完成测试'
    if request.method == 'POST':
        mbti_form = forms.MBTIForm(request.POST)
        answer_list = []
        if mbti_form.is_valid():
            message = '已完成测试'
            for i in range(len(mbti_form)):
                answer_list.append(mbti_form.cleaned_data[f'q{i}'])
            mbti_type = get_mbti_type(answer_list)
            user = models.User.objects.get(username=request.session['user_name'])
            user.mbti = mbti_type
            user.save()
            request.session['is_mbti'] = True
            request.session['user_mbti'] = user.mbti
            return redirect('/mbti/')

    mbti_form = forms.MBTIForm()
    return render(request, 'MBTI/test.html', locals())