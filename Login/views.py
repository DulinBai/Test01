# coding=utf-8
from django.shortcuts import render
from Register.models import User
from suds.client import Client

# Create your views here.
def login(request):
    if request.method == 'POST':
        id_num=request.POST.get('id_num')
        password_based=request.POST.get('password_based')

        """        
        client = Client("http://10.170.8.106:7789/?wsdl", cache=None)
        result = client.service.login(id_num, password_based)

        print(result)

        if result.string[0] == '1':
            return render(request, 'success.html')
        elif result.string[0] == '2':
            return render(request, 'fail02.html')
        elif result.string[0] == '3':
            return render(request, 'fail01.html')
        """




        if not User.objects.filter(id_num=id_num):
            return render(request, 'fail01.html')
        elif not User.objects.filter(id_num=id_num, password_based=password_based):
            return render(request, 'fail02.html')
        else:
            return render(request, 'success.html')

    return render(request, '../templates/login.html')

