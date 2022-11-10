from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
# Create your views here.

def index(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 if request.user.is_anonymous:
    return redirect('/login')
 return render(request, 'index.html', {'img':img, 'form':form})


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request, "login.html")

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect('/login')


def delete(request, id):
  item = Image.objects.get(id=id)
  item.delete()
  return redirect('/deleteimg')
  

def deleteimg(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Image.objects.all()
 if request.user.is_anonymous:
    return redirect('/login')
 return render(request, 'deleteimg.html', {'img':img, 'form':form})


    

	