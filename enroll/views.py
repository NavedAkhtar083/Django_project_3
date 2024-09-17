from django.shortcuts import render
from .forms import studentregistration

# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=studentregistration(request.POST)
    else:
        fm=studentregistration()
    return render(request,'enroll/addshow.html',{'form':fm})
