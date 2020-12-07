from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def result(request):
    inp_name = request.GET['name']
    inp_age = request.GET['age']
    inp_purpose = request.GET['purposelist']
    return render(request, 'result.html', {'home_name':inp_name, 'home_age':inp_age, 'home_purpose':inp_purpose})