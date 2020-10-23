from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

account = {}

# Create your views here.
def my_register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(username)>8:
            error = {'error':'账户长度不能超过八位数!'}
            return render(request,'register.html',error)
        else:
            username_all = [x for x in account]
            if username in username_all:
                error = {'error':'"{}"该用户名已经注册过!'.format(username)}
                return render(request,'register.html',error)

            else:
                if password.isalnum():
                    if len(password)>8:
                        error={'error':'密码长度不能超过八位数!'}
                        return render(request,'register.html',error)
                    else:
                        account[username] = password
                        return render(request,'register.html',messages.success(request,'成功注册！'))
                else:
                    error = {'error':'密码只能由数字和字母组成!'}
                    return render(request,'register.html',error)
            return render(request,'regiser.html',dict)


def my_homepage(request):
    if request.method == 'GET':
        return render(request,'homepage.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        username_all = [x for x in account]
        if username in username_all:
            if password == account[username]:
                return HttpResponse('成功登录！ <br>您的账户是:{} <br>您的密码是:{} '.format(username,password))
            else:
                error = {'error':'密码错误!'}
                return render(request,'homepage.html',error)
        else:
            error = {'error':'"{}"账号不存在!'.format(username)}
            return render(request,'homepage.html',error)
        return render(request,'homepage.html',dict)

