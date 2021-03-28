from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date


# Create your views here.

def  index(request):
    return render(request, 'index.html')

def  admin_login(request):
    error = ""
    if request.method == "POST":
        user_email = request.POST['email']
        user_passd = request.POST['password']
        user = authenticate(username=user_email, password=user_passd)
        
        if user.is_staff:
            login(request, user)
            error = "no"
        else:
            error="yes" 
   
    d = {"error":error} 

    return render(request, 'admin_login.html', d)

def  admin_home(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    return render(request, 'admin_home.html')    

def  user_login(request):
    error = ""
    if request.method == "POST":
        user_email = request.POST['email']
        user_passd = request.POST['password']
        user = authenticate(username=user_email, password=user_passd)
        
        if user:
            user_data = StudentUser.objects.get(user=user)
            if user_data.type == "student":
                login(request, user)
                error = "no"
            else:
                error="yes" 
        else:
            error="yes"
    d = {"error":error}                    
    return render(request, 'user_login.html', d)    

def  recruiter_login(request):
    error = ""
    if request.method == "POST":
        user_email = request.POST['email']
        user_passd = request.POST['password']
        user = authenticate(username=user_email, password=user_passd)
        
        if user:
            try:
                user_data = Recruiter.objects.get(user=user)
                if user_data.type == "recruiter" and user_data.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error="not" 
            except:
                error = "yes"        
        else:
            error="yes"
    d = {"error": error}
    print(d)                    

    return render(request, 'recruiter_login.html', d)  


def  recruiter_signup(request):
    error = ""
    if request.method == "POST":
        f_name   = request.POST['fname']
        l_name = request.POST['lname']
        image = request.FILES['image']
        password = request.POST['pwd']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        company = request.POST['company']

        try:
            user = User.objects.create_user(first_name=f_name, last_name=l_name, username=email, password=password)
            Recruiter.objects.create(user=user, mobile=contact, image=image, gender=gender, company=company, type='recruiter', status="pending")
            error = "no"
    
        except:
            error = "yes"
    d = {'error':error}        
    return render(request, 'recruiter_signup.html',d)     

def  Logout(request):
    logout(request)
    return redirect("index")      

def  user_home(request):
    if not request.user.is_authenticated:
        return redirect("user_login")

    return render(request, 'user_home.html')  

def  user_signup(request):
    error = ""
    if request.method == "POST":
        f_name   = request.POST['fname']
        l_name = request.POST['lname']
        image = request.FILES['image']
        password = request.POST['pwd']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']

        try:
            user = User.objects.create_user(first_name=f_name, last_name=l_name, username=email, password=password)
            StudentUser.objects.create(user=user, mobile=contact, image=image, gender=gender, type='student')
            error = "no"
    
        except:
            error = "yes"
    d = {'error':error}        

    return render(request, 'user_signup.html',d)        

def  view_user(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = StudentUser.objects.all()
    d = {'data':data}    

    return render(request, 'view_user.html', d) 

def  delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_user') 

def  recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect("admin_home")
    data = Recruiter.objects.filter(status="pending")
    d = {'data':data}    

    return render(request, 'recruiter_pending.html', d)     

def  recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = Recruiter.objects.filter(status="Accept")
    d = {'data':data}    

    return render(request, 'recruiter_accepted.html', d)   

def  recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = Recruiter.objects.filter(status="Reject")
    d = {'data':data}    

    return render(request, 'recruiter_rejected.html', d)  

def  recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = Recruiter.objects.all()
    d = {'data':data}    

    return render(request, 'recruiter_all.html', d)  

def  delete_recruiter(request, pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    data = User.objects.get(id=pid)
    data.delete()

    return render(request, 'recruiter_all.html', d)      


def  change_status(request, pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    error = ""    
    recruiter = Recruiter.objects.get(id=pid)

    if request.method == "POST":
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error = "no"
        except:
            error = "yes"
    d = {'recruiter':recruiter, 'error':error}    

    return render(request, 'change_status.html', d)     

def  change_password_admin(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    error = ""    
    if request.method == "POST":
        o = request.POST['password']
        n = request.POST['new_password']
        
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"    
        except:
            error = "yes"
    d = {'error':error}    

    return render(request, 'change_password_admin.html', d)     

def  change_password_user(request):
    if not request.user.is_authenticated:
        return redirect("user_login")
    error = ""    
    if request.method == "POST":
        o = request.POST['password']
        n = request.POST['new_password']
        
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"    
        except:
            error = "yes"
    d = {'error':error}    

    return render(request, 'change_password_user.html', d)     

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = ""
    if request.method == "POST":
        f_name   = request.POST['fname']
        l_name = request.POST['lname']
        contact = request.POST['contact']
        gender = request.POST['gender']

        recruiter.user.first_name = f_name
        recruiter.user.last_name = l_name
        recruiter.mobile = contact
        recruiter.gender = gender

        try:
            recruiter.save()
            recruiter.user.save()
            error = "no"
    
        except:
            error = "yes"

        try:
            image = request.FILES['image']
            recruiter.image = image
            recruiter.save()
            error = "no"
        except:
            pass
    
    d = {'recruiter':recruiter, 'error':error}    
    return render(request, "recruiter_home.html", d)

def  change_password_recruiter(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error = ""    
    if request.method == "POST":
        o = request.POST['password']
        n = request.POST['new_password']
        
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"    
        except:
            error = "yes"
    d = {'error':error}    

    return render(request, 'change_password_recruiter.html', d)     

def  add_job(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error = ""
    if request.method == "POST":
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal= request.POST['salary']
        exp = request.POST['experience']
        l = request.FILES['logo']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['desc']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter, start_date=sd, end_date=ed, title=jt, salary=sal, image=l, description=des, experience=exp, location=loc, skills=skills, creationdate=date.today())
            error="no"
        except:
            error="yes"
    d = {"error":error}               
    return render(request, 'add_job.html', d)  


def  job_list(request):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job':job}     
    return render(request, 'job_list.html', d)      

def  edit_job(request,pid):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == "POST":
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal= request.POST['salary']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['desc']

        job.title = jt
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = skills
        job.description = des
        try:
            job.save()
            error="no"
        except:
            error="yes"
        if sd:
            try:
                job.start_date = sd
                job.save()
            except:
                pass
        else:
            pass 

        if ed:
            try:
                job.end_date = ed
                job.save()
            except:
                pass
        else:
            pass    

    d = {"error":error, 'job':job}               
    return render(request, 'edit_jobdetail.html', d)  



def  change_companylogo(request,pid):
    if not request.user.is_authenticated:
        return redirect("recruiter_login")
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == "POST":
        cl = request.FILES['logo']
        job.image = cl
        try:
            job.save()
            error="no"
        except:
            error="yes"
        

    d = {"error":error, 'job':job}               
    return render(request, 'change_companylogo.html', d)  
