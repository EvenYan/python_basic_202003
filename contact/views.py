from django.shortcuts import render
from django.http import HttpResponse
from contact.models import PeopleInfo

# Create your views here.

def index(request):
    return HttpResponse("Hello Django!")


def home(request):
    people_list = PeopleInfo.objects.all()
    context = {"people_list": people_list}
    return render(request, "contact/index.html", context=context)


def detail(request, id):
    p = PeopleInfo.objects.get(id=id)
    context = {"people": p}
    return render(request, "contact/detail.html", context=context)


def register(request):
    return render(request, "contact/register.html")


def deal_register(request):
    from contact.tools import gen_secret
    username = request.POST.get("username")
    passwd = request.POST.get("passwd")
    passwd = gen_secret(passwd)
    phone_num = request.POST.get("phone_num")
    
    PeopleInfo.objects.create(name=username, passwd=passwd, phone_num=phone_num)

    return HttpResponse("%s注册成功" %username)