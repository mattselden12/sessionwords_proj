from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context= {
        
    }
    return render(request, 'session_words/index.html', context)

def clear(request):
    pass