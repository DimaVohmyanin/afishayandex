from django.shortcuts import render
from django.http import HttpResponseGone

def show_page(request):
    print('Кто-то зашёл на главную')
    return render(request, 'testapp/index.html')