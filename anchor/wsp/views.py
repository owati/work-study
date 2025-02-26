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
            except Exception as e:  
                print(e)
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

    
    #NOTE: I also made some changes to the edit html
    
    student = Student.objects.get(id=id) # fetches the student with that id

    recommendation = None
    try:
        recommendation = student.recommendation # raise error if no recommendation has been created
    except:
        pass

    form = RecommendationForm(instance=recommendation)

    if request.method == 'POST':
        form = RecommendationForm(request.POST, instance=recommendation) # popultaes the form with the new data
        form2 = StudentForm(request.POST, instance=student)

        # print(dict(form2.errors), request.POST)
        
        #print(dict(form.errors), request.POST)
        if form.is_valid() and form2.is_valid():
            recommendation_data = form.save(commit=False) # creates instance of new recommendation but does not save to the data base because we want to attach the student model to it
            recommendation_data.student = student # assign the student model to it
            recommendation_data.save()  

            form2.save()
            return redirect("/show") 

    return render(request, 'edit.html', {'student': student, 'form' : form}) #'form1': form1 

def destroy(request, id):  
    student = Student.objects.get(id=id)  
    student.delete()  
    return redirect("/show")  