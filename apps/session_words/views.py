from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    if 'words' in request.session:
        context= {
            "words": request.session['words'],
        }
    else:
        context={
            "words": None
        }
    return render(request, 'session_words/index.html', context)

def process(request):
    temptime= strftime("%#I:%M:%S%p, %B %#d %Y", localtime())
    if 'big_font' in request.POST:
        big_font='36px'
    else:
        big_font='20px'
    if 'words' not in request.session:
        request.session['words']= [{"word": request.POST['word'], "color": request.POST['color'], "fontsize": big_font, "datetime": temptime}]
        print(request.session['words'])
    else:
        x={"word": request.POST['word'], "color": request.POST['color'], "fontsize": big_font, "datetime": temptime}
        temp_list = request.session['words']
        real_temp = [x]+temp_list
        request.session['words'] = real_temp
        print(request.session['words'])
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')