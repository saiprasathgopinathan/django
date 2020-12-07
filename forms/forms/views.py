from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def result(request):
    inp = request.GET['user_input']
    return render(request, 'result.html',{'home_input':inp.upper()})    