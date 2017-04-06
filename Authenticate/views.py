#coding:utf-8
from django.shortcuts import render
import json
from suds.client import Client
from django.http import HttpResponseRedirect
from django.http import HttpResponse

global client
client = Client("http://10.170.27.64:7789/?wsdl", cache=None)

def authenticate(request):

    global client

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        login_result = client.service.login(username, password)

        Piece_dict3 = {
            "flag_user" : True,
            "flag_pass" : True,
            "flag_cert" :True
        }

        if login_result == '1':
            request.session[username] = password
            return HttpResponse(json.dumps(Piece_dict3))
            #return HttpResponseRedirect('/user/')
        elif login_result == '2':
            Piece_dict3["flag_pass"]=False
            print('口令错误')
            return HttpResponse(json.dumps(Piece_dict3))
        elif login_result == '3':
            Piece_dict3["flag_user"]=False
            print('用户名不存在')
            return HttpResponse(json.dumps(Piece_dict3))
        else:
            pass

    else:
        return render(request, '../templates/authenticate.html')