# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from Register.models import User
from Register.form import RegisterFrom



# Create your views here.
def register(request):
    if request.method == "POST":
        RF = RegisterFrom(request.POST)
        if RF.is_valid():
            #获取表单信息
            id_num = RF.cleaned_data['id_num']
            password_based = RF.cleaned_data['password_based']
            username = request.POST.get('username')
            gender = request.POST.get('gender')
            unit = request.POST.get('unit')
            position = request.POST.get('position')
            partjob = request.POST.get('partjob')
            scheme = request.POST.get('scheme')
            ans = {}
            ans['id_num'] = id_num

            filterResult = User.objects.filter(id_num=id_num)
            if len(filterResult) > 0:
                return render_to_response('register_fail.html', ans)
            else:
                #将表单写入数据库
                User.objects.create(id_num=id_num, username=username, gender=gender, unit=unit, position=position,
                                    partjob=partjob, scheme=scheme, password_based=password_based)
                #返回注册成功页面
                return render_to_response('register_success.html', ans)
    else:
        RF = RegisterFrom()
    return render_to_response('../templates/register.html', {'RF': RF})