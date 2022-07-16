from django.shortcuts import render, redirect  
from django.http import HttpResponse
from .forms import *
from .models import *  

# Create your views here.  
def home(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)
        print(dict(form.errors))
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponse("<h3>Application successfully submitted!</h3><br><center><a href='' class='btn btn-primary'>Apply to Work Study Programme</a></center>")
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'home.html',{'form':form})  
def show(request):  
    students = Student.objects.all()  
    return render(request,"show.html",{'students':students})  
def edit(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'edit.html', {'student':student})  
def update(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student) 
    # form1 = RecommendationForm(request.POST, instance = form) 
    if form.is_valid():  
        form.save()  
        return redirect("/show")  

    # if request.method == "POST":  
    #     form1 = RecommendationForm(request.POST)
    #     print(dict(form.errors))
    #     if form.is_valid():  
    #         if form1.is_valid():
    #             try:  
    #                 form.save()
    #                 form1.save()  
    #                 return HttpResponse("<h3>Application successfully submitted!</h3><br><center><a href='' class='btn btn-primary'>Apply to Work Study Programme</a></center>")
    #             except:  
    #                 pass  
    # else:  
    #     form = RecommendationForm()  
    return render(request, 'edit.html', {'student': student}) #'form1': form1 
def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  