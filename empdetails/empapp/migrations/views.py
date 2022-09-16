from django.shortcuts import render,redirect
from empapp.models import employee
from empapp.forms import empform
from django.contrib import admin
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not none:
            auth.login(request,user)
            return redirect("/")
        else:
           messages.info(request,'invalid credentials')
           return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method =='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,)
                user.save():
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')




def empapp(request):
     name="jone"
     emp_data=employee.objects.all()
     emp_dict={"emp_list":emp_data}
     return render(request,"empapp/index.html",context = emp_dict)
# Create your views here.
def create_view(request):
    form=empform()
    if request.method =='POST':
        form=empform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/employee')

    return render(request,'empapp/create.html',{'form':form})

def delete_view(request ,id):
    emp_data = employee.objects.get(id=id)
    emp_data.delete()
    return redirect('/employee')

def update_view(request,id):
    emp_data = employee.objects.get(id=id)
    if request.method =='POST':
        form = empform(request.POST,instance=emp_data)
        if form.is_valid():
            form.save()
            return redirect('/employee')


    return render(request,"empapp/update.html" ,{"employee" :emp_data})