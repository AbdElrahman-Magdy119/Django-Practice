from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.


def liststudent(r):
    return HttpResponseRedirect('/student')

def liststaff(r):
    return HttpResponseRedirect('/staff')


def link(r):
    if(r.method=='GET'):
        return render(r,'reports/report.html')