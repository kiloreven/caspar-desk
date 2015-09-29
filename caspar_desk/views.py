from django.shortcuts import render
from .utils import pp24_simplesuper

def test(request):
    template = 'desk/test.html'

    context = {}
    return render(request, template, context)

def pp24_admin(request):
    template = 'desk/pp24_admin.html' 
    context = {}

    if request.method == 'POST':
        data = request.POST
        print data
        pp24_simplesuper(
            request.POST.get('test1'),
            request.POST.get('test2'))

    return render(request, template, context)
