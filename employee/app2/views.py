from django.shortcuts import render
from app2.models import Student
def home(request):

    return render(request, 'home.html')
def add(request):
    if(request.method=="POST"):

        en=request.POST['en']
        ag=request.POST['ag']
        ad=request.POST['ad']
        e=request.POST['e']
        c=request.FILES['i']

        b=Student.objects.create(ename=en,age=ag,address=ad,email=e,cover=c)
        b.save()
        return home(request)
    return render(request,'add.html')

def edit(request,i):
    k=Student.objects.get(id=i)
    if(request.method=="POST"):
        k.ename=request.POST['en']
        k.age=request.POST['ag']
        k.address=request.POST['ad']
        k.email=request.POST['e']

        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES.get('i')

        k.save()
        return view_details(request)
    return render(request,'edit.html',{'Student':k})

def view_details(request):
    k=Student.objects.all()
    return render(request,'view.html',{'Student':k})



def delete(request,p):
    k=Student.objects.get(id=p)
    k.delete()
    return view_details(request)

