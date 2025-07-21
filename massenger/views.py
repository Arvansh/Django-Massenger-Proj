from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import Message

def user_login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('group_chat')
    else:
      return render(request, 'massenger/login.html', {'error':'Invalid username or password.'})
  return render(request, 'massenger/login.html')

def user_register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    else:
      print(form.errors)
      return render(request, 'massenger/register.html', {'form': form})
  
  else:
    form = UserCreationForm()
    return render(request, 'massenger/register.html', {'form': form})
  
def user_logout(request):
  logout(request)
  return redirect('login')

@login_required
def group_chat(request):
  if request.method == "POST":
    content = request.POST['content']
    if content:
      Message.objects.create(user=request.user, content=content)
      return redirect('group_chat')
    #if request.user.is_authenticated:
    #  return render(request, 'group_chat.html')
    #else:
    #  return redirect('login')
  messages = Message.objects.all().order_by('timestamp')
  return render(request, 'group_chat.html', {'messages':messages})

@login_required
def clear_chat(request):
  if request.user.is_superuser:
    Message.objects.all().delete()
  return redirect('group_chat')