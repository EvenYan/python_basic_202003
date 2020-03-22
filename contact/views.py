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