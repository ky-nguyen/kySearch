from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def projects(request):
    return HttpResponse('Here Are our products')


def project(request, pk):
    return HttpResponse('SINGLE PROJECT' + ' ' + str(pk))