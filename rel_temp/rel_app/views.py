from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'rel_app/index.html')

def other(request):
    contexts = {'text':'hello word','number':100}
    return render(request,'rel_app/other.html',contexts)

def relative(request):
    return render(request,'rel_app/relative.html')

def base(request):
    return render(request,'rel_app/base.html')



