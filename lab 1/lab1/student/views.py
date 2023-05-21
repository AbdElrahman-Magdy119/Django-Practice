from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.

def index(req):
    if(req.method=='GET'):
        res= HttpResponse('student view')
        return res
    else:
        return HttpResponse('access denied')
def insert(r):
    if(r.method=='GET'):
        return render(r,'student/insert.html')

def update(r):
    if(r.method=='GET'):
        return render(r,'student/update.html')

def delete(r):
    return HttpResponseRedirect('/student')

