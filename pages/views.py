from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def homePageView(request):
    template = loader.get_template('pages/index.html')
    context = {
        'fullName': 'Kim'
    }

    return HttpResponse(template.render(context, request))
def detailPage(request):
    return HttpResponse("Hello")
