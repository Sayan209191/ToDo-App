import json
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from task.models import Task 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.




# sign up 
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        username=request.POST["name"]
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')                   
        try:
            if User.objects.get(username=email):
                # return HttpResponse("email already exist")
                messages.info(request,"Email is Taken")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(username,email,password)
        user.is_active=True
        user.save()
        return redirect('/login')
    return render(request,"signup.html")


# sign in
def handlelogin(request):
    if request.method=="POST":

        username=request.POST['username']
        userpassword=request.POST['pass']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/home')

        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')

    return render(request,'login.html')  

# logout
def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/')



def index(request):
    return render(request, "index.html")

@login_required(login_url='/login')
def home(request):
    task = Task.objects.filter(user=request.user).all()
    return render(request,"index.html", {'task':task})
    

@login_required(login_url='/login')
def addTask(request):
    if request.method == 'POST':
        print(request.POST.get('title'))
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        # Create a Task and associate it with the current user
        task = Task.objects.create(
            title=title, 
            description=description, 
            due_date=due_date, 
            user=request.user
        )
        task.save()

        return redirect('/home')

    return render(request, 'addtask.html')

@login_required(login_url='/login')
def editTask(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        
        
        task.title = title;
        task.description = description;
        task.due_date = due_date;
        task.complete = 'complete' in request.POST
        task.save()
        return redirect('/home')
    else:
        return render(request, 'edittask.html', {'task': task})

def calender(request) :
    return render(request, 'calender.html')