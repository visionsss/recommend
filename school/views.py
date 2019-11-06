from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import form
school_name = ''
city = ''


def school(request):
    global school_name, city
    if request.method == 'POST':
        school_name = request.POST.get('school_name')
        city = request.POST.get('city')
        school_list = models.school_info.objects.filter(name__contains=school_name, city__contains=city)
    school_list = models.school_info.objects.filter(name__contains=school_name, city__contains=city)
    paginator = Paginator(school_list, 10)  # 设置每一页显示几条  创建一个panginator对象
    last = paginator.num_pages
    try:
        current_num = int(request.GET.get('page', 1))  # 当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        school_list = paginator.page(current_num)

    except EmptyPage:
        current_num = last
        school_list = paginator.page(last)  # 当你输入的page是不存在的时候就会报错

    if paginator.num_pages > 11:  # 如果分页的数目大于11
        if current_num - 5 < 1:  # 你输入的值
            pageRange = range(1, 11)  # 按钮数
        elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
            pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数

        else:
            pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示

    else:
        pageRange = range(1, last)  # 正常分配

    school_form = form.school_form(initial={'school_name': school_name, 'city': city})
    return render(request, 'school/school.html', locals())
