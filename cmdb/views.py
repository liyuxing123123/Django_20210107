#encoding:utf-8
from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def login(request):
    return HttpResponse('cmdb')

from cmdb import models

def business(request):
    v1 = models.Business.objects.all()

    v2 = models.Business.objects.all().values('id', 'caption')

    v3 = models.Business.objects.all().values_list('id', 'caption')

    return render(request, 'business.html', {'v1':v1,'v2':v2,'v3':v3})

def orm(request):
    # models.UserInfo.objects.create(username='root',password='123')
    # dic = {'username':'eric', 'password':'666'}
    # models.UserInfo.objects.create(**dic)
    # obj = models.UserInfo(username='root', password='123')
    # obj.save()

    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='root')
    # for row in result:
    #     print(row.id,row.username,row.password)

    # models.UserInfo.objects.filter(id=2).delete()

    models.UserInfo.objects.all().update(password='999')

    return HttpResponse('orm')



# def login(request):
#     # string = """
#     # <form>
#     #     <input type = 'text'/>
#     # </form>
#     # """
#     # f = open('templates/login.html', 'r', encoding="utf-8")
#     # data = f.read()
#     # f.close()
#     # return HttpResponse(data)
#     return render(request, 'login.html')
# def login(request):
#     # error_msg = ""
#     # if request.method == "POST":
#     #     #获取用户通过POST提交过来的数据
#     #     user = request.POST.get('user', None)
#     #     pwd = request.POST.get('pwd', None)
#     #     if user == 'root' and pwd == '123':
#     #         return redirect('/home')
#     #     else:
#     #         #用户名密码错误
#     #         error_msg = "用户名或密码错误"
#     # return render(request, 'login.html', {'error_msg':error_msg})
#
#     if request.method == "GET":
#         return render(request, 'login.html')
#     elif request.method == "POST":
#
#         # v1 = request.POST.get('gender')
#         # print(v1)
#         #
#         # v2 = request.POST.getlist('favor')
#         # print(v2)
#         #
#         # v3 = request.POST.getlist('city')
#         # print(v3)
#
#         obj = request.FILES.get('fileupload')
#         print(obj, type(obj), obj.name)
#         import os
#         file_path = os.path.join('upload', obj.name)
#         f = open(file_path, mode='wb')
#         for i in obj.chunks():
#             f.write(i)
#         f.close()
#
#         return render(request, 'login.html')
#
# from django.views import View
# class Home(View):
#     def dispatch(self, request, *args, **kwargs):
#         print('before')
#         result = super(Home, self).dispatch(request, *args, **kwargs)
#         print('after')
#         return result
#
#     def get(self, request):
#         print(request.method)
#         return render(request, 'home.html')
#
#     def post(self,request):
#         print(request.method, 'POST')
#         return render(request, 'home.html')
#
#
# # def home(request):
# #     if request.method == "POST":
# #         u = request.POST.get('username')
# #         e = request.POST.get('email')
# #         g = request.POST.get('gender')
# #
# #         temp = {'username':u, 'email':e, 'gender':g}
# #         USER_LIST.append(temp)
# #
# #     return render(request, 'home.html', {'user_list': USER_LIST})
#
# # def home(request):
# #     return HttpResponse('<h1>Hello</h1>')
#
# USER_LIST = [
#     {'username':'alex', 'email':'test1@eq.com', 'gender':'男'},
#     {'username':'bob', 'email':'test2@eq.com', 'gender':'男'},
#     {'username':'seven', 'email':'test3@eq.com', 'gender':'男'},
# ]
#
# USER_DICT = {
#     '1':{'name':'root1', 'email':'root@live.com'},
#     '2':{'name':'root2', 'email':'root@live.com'},
#     '3':{'name':'root3', 'email':'root@live.com'},
#     '4':{'name':'root4', 'email':'root@live.com'},
#     '5':{'name':'root5', 'email':'root@live.com'},
# }
#
# def index(request):
#     return render(request, 'index.html', {'user_dict':USER_DICT})
#
# # def detail(request):
# #     nid = request.GET.get('nid')
# #     detail_info = USER_DICT[nid]
# #     return render(request, 'detail.html', {'detail_info':detail_info})
#
# def detail(request,nid):
#     # return HttpResponse(nid)
#     # nid = request.GET.get('nid')
#     detail_info = USER_DICT[nid]
#     return render(request, 'detail.html', {'detail_info':detail_info})