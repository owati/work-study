from django.db import models

# Create your models here.
class Student(models.Model):
    sur_name = models.CharField(max_length=150)
    mid_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    matric_no = models.CharField(max_length=35)  
    phone = models.CharField(max_length=20)  
    email = models.EmailField()  
    LEVEL = (('LEVEL', 'Level'), ('200', '200'), ('300', '300'), ('400', '400'))
    level = models.CharField(max_length=5, choices = LEVEL, default='LEVEL')
    dob = models.DateField()  
    gender_choice = (('GENDER', 'Gender'),('MALE', 'Male'), ('FEMALE', 'Female'))
    gender = models.CharField(max_length=10, choices = gender_choice, default ='GENDER' ) 
    fac_choice = (('FACULTY', 'Faculty'), ('HUMANITIES', 'Faculty of Humanities'), ('SMS', 'Faculty of Social and Management Sciences'), ('SCIENCE', 'Faculty of Science and Science Education')) 
    faculty = models.CharField(max_length=5, choices = fac_choice, default = 'FACULTY')  
    department = models.CharField(max_length=300)
    session_choices = (('SESSION', 'Session'), ('21/22', '2021/2022'), ('22/23', '2022/2023'), ('23/24', '2023/2024'), ('24/25', '2024/2025'))
    session = models.CharField(max_length=50, choices = session_choices, default ='SESSION') 
    semester_choices = (('SEMESTER', 'Semester'), ('FIRST', '1st Semester'), ('SECOND', '2nd Semester'))
    semester = models.CharField(max_length=50, choices = semester_choices, default='SEMESTER') 
    cgpa_choices = (('CGPA', 'CGPA'), ('BELOW1', 'Below 1'), ('BETWEEN12', 'Between 1 and 2'), ('BETWEEN23', 'Between 2 and 3'), ('ABOVE3', 'Above 3'))
    cgpa = models.CharField(max_length=50, choices = cgpa_choices, default='CGPA') 
    reason1 = models.TextField()
    reason2 = models.TextField(blank= True)  
    reason3 = models.TextField(blank= True)  
    psur_name = models.CharField(max_length=150)
    pmid_name = models.CharField(max_length=150)
    pfirst_name = models.CharField(max_length=150)
    occupation = models.CharField(max_length=70)  
    pphone = models.CharField(max_length=20)  
    pemail = models.EmailField()
    app_choice = (('YES', 'Yes'), ('NO', 'No'), ('DONT_KNOW', "Don't Know"))
    parent_approval = models.CharField(max_length=5, choices = app_choice, default='DONT_KNOW')
    library = models.BooleanField(default = False, blank= True)
    cafetaria = models.BooleanField(default = False, blank= True)
    supermarket = models.BooleanField(default = False, blank= True)
    ict_unit = models.BooleanField(default = False, blank= True)
    water_works = models.BooleanField(default = False, blank= True)
    general_affairs = models.BooleanField(default = False, blank= True)
    others = models.CharField(max_length=50, blank= True)
    preferred = models.CharField(max_length=50, blank=True)
    YES = 'Yes' 
    NO = 'No'
    exp_choice = [(YES, 'Yes'), (NO, 'No'), ('DONT_KNOW', "I don't think so")]
    experience = models.CharField(max_length=20, choices = exp_choice , default='DONT_KNOW')  
    expdet = models.TextField(blank= True) 
    hrs = models.IntegerField()  
    declaration = models.CharField(max_length=150) 
    namesign = models.CharField(max_length=150)  
    sign = models.FileField(upload_to='sign/',blank= True)
    hodrec = models.TextField(blank= True) 
    hodname = models.CharField(max_length=150, blank= True)  
    hod_date = models.DateField()  
    hodsign = models.FileField(upload_to='sign/', blank= True)
    deanrec = models.TextField(blank= True) 
    deanname = models.CharField(max_length=150, blank= True)  
    dean_date = models.DateField()  
    deansign = models.FileField(upload_to='sign/',blank= True)
    dsacom = models.TextField(blank= True) 
    dsaname = models.CharField(max_length=150, blank= True)  
    dsa_date = models.DateField()  
    dsasign = models.FileField(upload_to='sign/',blank= True)
    pconsent = models.FileField(upload_to='pconsent/',blank= True)
    unithead_comm= models.TextField(blank= True)
    unithead_name = models.CharField(max_length=150, blank= True)  
    unithead_date = models.DateField()  
    unithead_sign = models.FileField(upload_to='sign/', blank= True) 
    wspcomm = models.TextField(blank= True) 
    wspname = models.CharField(max_length=150, blank= True)  
    wsp_date = models.DateField()  
    wspsign = models.FileField(upload_to='sign/', blank= True)
    unit_choices = (('CAFETERIA', 'Cafeteria'), ('LIBRARY', 'Library'), ('SUPERMARKET', 'Supermarket'), ('ICT UNIT', 'ICT Unit'), ('WATER WORKS', 'Water Works'), ('GENERAL AFFAIRS', 'General Affairs(Cleaning)')) 
    unit_posted = models.CharField(max_length=8, choices = unit_choices)
    recomend_critchoice = (('RECOMMENDED', 'Recommended for Approval'), ('NOT RECOMMENDED', 'Not Recommended'))
    recomend_crit = models.CharField(max_length=4, choices = recomend_critchoice)
    vcapprove_choice = (('APPROVED', 'Approved'), ('NOT APPROVED', 'Not Approved'))
    vcapprove = models.CharField(max_length=4, choices = vcapprove_choice)
    
    class Meta:
        db_table = "student"   