from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.

def index(req):
    if(req.method=='GET'):
        res= HttpResponse('staff view')
        return res
    else:
        return HttpResponse('access denied')
    
def insert(r):
    return JsonResponse({'id':1,'action':'insert'})


def update(r):
     return JsonResponse({'id':1,'action':'update'})

def delete(r):
    return HttpResponseRedirect('/staff')


