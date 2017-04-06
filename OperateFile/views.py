#coding=utf8
from django.shortcuts import render
import json
from django.http import HttpResponse
from suds.client import Client

global client
client = Client("http://10.170.27.64:7789/?wsdl", cache=None)


def operatefile(request):

    global client

    if request.method == 'GET':

        id_num = request.GET.get('username')
        print(id_num)
        password_based = request.session[id_num]

        file_result = client.service.files(id_num, password_based)
        file_num = len(file_result.stringArray)

        filelist = []  # 只有文件名的文件信息

        for i in range(0, file_num):
            file = {
                'filename': file_result.stringArray[i].string[0],
                "file_content": '',
                'filesize': '',
                "modify_time": '',
                "authority": '',
                "read_authority": False,
                "edit_authority": False,
            }
            filelist.append(file)

        Piece_dict2 = {
            "file_num": file_num,
            "delete_authority": False,
            "file": filelist
        }

        return render(request, '../templates/file_test.html', {'username01': id_num,
                                                               'Piece_dict2': json.dumps(Piece_dict2)})

    if request.method == 'POST':

        control = request.POST.get('control')

        if control == '1':

            filen_read = request.POST.get('filen_read')
            usern_read = request.POST.get('usern_read')
            password_based = request.session[usern_read]

            file_result = client.service.files(usern_read, password_based)
            file_num = len(file_result.stringArray)

            filelist = []  # 只有文件名的文件信息

            for i in range(0, file_num):
                file = {
                    'filename': file_result.stringArray[i].string[0],
                    "file_content": '',
                    'filesize': '',
                    "modify_time": '',
                    "authority": '',
                    "read_authority": False,
                    "edit_authority": False,
                }
                filelist.append(file)

            Piece_dict2 = {
                "file_num": file_num,
                "delete_authority": False,
                "file": filelist
            }

            read_result = client.service.read(usern_read, filen_read)

            for i in range(0, file_num):

                if filelist[i]['filename'] == filen_read:
                    if read_result.string[0] == '1':
                        filelist[i]['read_authority'] = True
                        filelist[i]['file_content'] = read_result.string[1]
                    else:
                        pass
                else:
                    pass

            return HttpResponse(json.dumps(Piece_dict2))#直接返回json对象不跳转

        elif control == '2' :




            usern_edit = request.POST.get('usern_edit')
            name_edit = request.POST.get('name_edit')
            content_edit = request.POST.get('content_edit')

            password_based = request.session[usern_edit]

            file_result = client.service.files(usern_edit, password_based)
            file_num = len(file_result.stringArray)

            filelist = []  # 只有文件名的文件信息

            for i in range(0, file_num):
                file = {
                    'filename': file_result.stringArray[i].string[0],
                    "file_content": '',
                    'filesize': '',
                    "modify_time": '',
                    "authority": '',
                    "read_authority": False,
                    "edit_authority": False,
                }
                filelist.append(file)

            Piece_dict2 = {
                "file_num": file_num,
                "delete_authority": False,
                "file": filelist
            }


            edit_result = client.service.edit(usern_edit, name_edit, content_edit)

            for i in range(0, file_num):
                if filelist[i]['filename'] == name_edit:
                    if edit_result == 1:
                        filelist[i]['edit_authority'] = True
                    else:
                        pass
                else:
                    pass

            return HttpResponse(json.dumps(Piece_dict2))#直接返回json对象不跳转

        elif control == '3':

            filen_dele = request.POST.get('filen_dele')
            usern_dele = request.POST.get('usern_dele')

            password_based = request.session[usern_dele]

            file_result = client.service.files(usern_dele, password_based)
            file_num = len(file_result.stringArray)

            filelist = []  # 只有文件名的文件信息

            for i in range(0, file_num):
                file = {
                    'filename': file_result.stringArray[i].string[0],
                    "file_content": '',
                    'filesize': '',
                    "modify_time": '',
                    "authority": '',
                    "read_authority": False,
                    "edit_authority": False,
                }
                filelist.append(file)

            Piece_dict2 = {
                "file_num": file_num,
                "delete_authority": False,
                "file": filelist
            }


            dele_result = client.service.delete(usern_dele, filen_dele)

            for i in range(0, file_num):
                if filelist[i]['filename'] == filen_dele:
                    if dele_result == 1:
                        print("Piece_dict2")
                        Piece_dict2["delete_authority"] = True
                    else:
                        pass
                else:
                    pass
                return HttpResponse(json.dumps(Piece_dict2))  # 直接返回json对象不跳转
        else:
            pass


#from Register.models import User

def user_info(request):

    global client
    if request.method == "GET":

        id_num = request.GET.get('username')

        password_based = request.session[id_num]

        user_result = client.service.user(id_num, password_based)

        Piece_dict1 = {
            'username':user_result.string[0],
            'gender':user_result.string[1],
            'unit':user_result.string[2],
            'position':user_result.string[3],
            'field':user_result.string[4]
        }

        # piece = User.objects.get(id_num="你不好")
        # Piece_dict1 = {
        #     'username':piece.username,
        #     'gender':piece.gender,
        #     'unit':piece.unit,
        #     'position':piece.position,
        #     'field':"域内"
        # }

        file_result = client.service.files(id_num, password_based)

        file_num = len(file_result.stringArray)

        filelist = []

        for i in range(0, file_num):

            file = {
                'filename' : file_result.stringArray[i].string[0],
                'filesize': file_result.stringArray[i].string[1],
                "modify_time": file_result.stringArray[i].string[2],
                "authority": file_result.stringArray[i].string[3]
            }
            filelist.append(file)

        Piece_dict2 = {

            "file_num":file_num,
            "file":filelist
        }
        return render(request, 'user_final.html', {'Piece_dict1':json.dumps(Piece_dict1),
                                                   'Piece_dict2':json.dumps(Piece_dict2),
                                                   'username01': id_num,})

    if request.method == 'POST':
        return render(request, '../templates/user_final.html')




