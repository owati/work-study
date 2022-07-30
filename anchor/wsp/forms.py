from django import forms  
from .models import *  

class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  

        widgets = {
            'sur_name': forms.TextInput(attrs={'class': 'container', 'placeholder': 'Surname'}),
            'mid_name': forms.TextInput(attrs={'class': 'container', 'placeholder': 'Middle Name'}),
            'first_name': forms.TextInput(attrs={'class': 'container', 'placeholder': 'First Name'}),
            'matric_no': forms.TextInput(attrs={'class': 'container', 'placeholder': 'Matric No'}),
            'phone': forms.TextInput(attrs={'class': 'container', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'container', 'placeholder': 'Email'}),
            'level': forms.Select(attrs={'class': 'container'}),
            'dob': forms.DateInput(attrs={'class': 'container', 'placeholder': 'yyyy-mm-dd'}),
            'gender': forms.Select(attrs={'class': 'container'}),
            'faculty': forms.Select(attrs={'class': 'container'}),
            'department': forms.TextInput(attrs={'class': 'container', 'placeholder': 'Department'}),
            'session': forms.Select(attrs={'class': 'container'}),
            'semester': forms.Select(attrs={'class': 'container'}),
            'cgpa': forms.Select(attrs={'class': 'container'}),
            'reason1': forms.Textarea(attrs={'class': 'container', 'placeholder': '1st Reason', 'rows':3}),
            'reason2': forms.Textarea(attrs={'class': 'container', 'placeholder': '2nd Reason', 'rows':3}),
            'reason3': forms.Textarea(attrs={'class': 'container', 'placeholder': '3rd Reason', 'rows':3}),
            'psur_name': forms.TextInput(attrs={'class': 'container', 'placeholder': 'Surname'}),
            'pmid_name': forms.TextInput(attrs={'class': 'container', 'placeholder': 'Middle Name'}),
            'pfirst_name': forms.TextInput(attrs={'class': 'container', 'placeholder': 'First Name'}),
            'occupation': forms.TextInput(attrs={'class': 'container', 'placeholder': 'Occupation'}),
            'pphone': forms.TextInput(attrs={'class': 'container', 'placeholder': 'Phone Number'}),
            'pemail': forms.EmailInput(attrs={'class': 'container', 'placeholder': 'Email'}),
            'parent_approval': forms.Select(attrs={'class': 'container'}),
            'experience': forms.Select(attrs={'class': 'container'}),
            'expdet': forms.Textarea(attrs={'class': 'container', 'placeholder': 'If yes, give details', 'rows':3}),
            'preferred': forms.TextInput(attrs={'class': 'container', 'placeholder': 'If you chose more than one in the above question, state your most preferred option'}),
            'hrs': forms.NumberInput(attrs={'class': 'container', 'placeholder': 'Hours per week'}),
        }


class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = "__all__"

        widgets = {
            'hodrec' : forms.Textarea(attrs={'class': 'container', 'placeholder': "HOD'S Recommendation", 'rows':3}),
            'hodname' : forms.TextInput(attrs={'class': 'container', 'placeholder': 'Full Name'}),
            'hod_date' : forms.DateInput(attrs={'class': 'container', 'placeholder': 'yyyy-mm-dd'}),
            'deanrec' : forms.Textarea(attrs={'class': 'container', 'placeholder': "HOD'S Recommendation", 'rows':3}),
            'deanname' : forms.TextInput(attrs={'class': 'container', 'placeholder': 'Full Name'}),  
            'dean_date' : forms.DateInput(attrs={'class': 'container', 'placeholder': 'yyyy-mm-dd'}),
            'dsacom' : forms.Textarea(attrs={'class': 'container', 'placeholder': "HOD'S Recommendation", 'rows':3}),
            'dsaname' : forms.TextInput(attrs={'class': 'container', 'placeholder': 'Full Name'}), 
            'dsa_date' : forms.DateInput(attrs={'class': 'container', 'placeholder': 'yyyy-mm-dd'}), 
            'unithead_comm': forms.Textarea(attrs={'class': 'container', 'placeholder': "HOD'S Recommendation", 'rows':3}),
            'unithead_name' : forms.TextInput(attrs={'class': 'container', 'placeholder': 'Full Name'}),  
            'unithead_date' : forms.DateInput(attrs={'class': 'container', 'placeholder': 'yyyy-mm-dd'}), 
            'wspcomm' : forms.Textarea(attrs={'class': 'container', 'placeholder': "HOD'S Recommendation", 'rows':3}), 
            'wspname' : forms.TextInput(attrs={'class': 'container', 'placeholder': 'Full Name'}),  
            'wsp_date' : forms.DateInput(attrs={'class': 'container', 'placeholder': 'yyyy-mm-dd'}), 
        }