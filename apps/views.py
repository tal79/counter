from django.shortcuts import render, redirect 

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] +=1
    return render(request, 'index.html')
