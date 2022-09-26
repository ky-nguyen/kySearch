from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


projectList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Build your ecommerce website with Shopify.'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'The striking portfolio websites in this selection demonstrate a unique approach to web design and plenty of personality.'
    },
    {
        'id': '3',
        'title': 'Social Website',
        'description': 'Reddit is a social news and entertainment website with tons of sub-communities dedicated to specific interests'
    },
]


def projects(request):
    page = 'Hello Ky'
    number = 10
    context = {
        'page': page,
        'number': number,
        'projects': projectList
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
