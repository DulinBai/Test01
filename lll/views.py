# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from Register.models import User
from django.core.serializers import serialize
import json

# Create your views here.
def lll(request):
    return render(request, 'lll.html')

def user(request):
    piece = User.objects.get(id_num="你不好")
    Piece_dict1 = {
        'id_num':piece.id_num,
        'username':piece.username,
        'gender':piece.gender,
        'unit':piece.unit,
        'position':piece.position,
        'partjob':piece.partjob,
        'scheme':piece.scheme,
        'password_based':piece.password_based,
        'field':"域内"
    }
    file1 = {
        'filename' : 'hahah',
        'filesize':"9999",
        "modify_time":"19930602",
        "authority":'读写'
    }
    file2 = {
        'filename' : 'hah',
        'filesize':"9999",
        "modify_time":"19930602",
        "authority":'读写'
    }
    Piece_dict2 = {
        "file_num":2,
        "file":[
            file1,file2
    ]

    }
    print(piece)
    return render(request, 'user.html', {'Piece_dict1':json.dumps(Piece_dict1),
                                         'Piece_dict2':json.dumps(Piece_dict2)})

def demo(request):
    username = request.GET.get('username')
    print(username)
    ans = {}
    ans['username'] = username
    return render(request, 'lll.html', ans)


from suds.client import Client


def readfile(request):
    client = Client("http://10.170.8.106:7789/?wsdl", cache=None)
    result = client.service.read(1101120700, "file1.txt")
    if result.string[0] == "1":
        ans = {}
        ans['file'] = result.string[1]
        with open("file1.txt","w") as f:
            f.write(result.string[1])

    return render(request, 'readfile.html', ans)