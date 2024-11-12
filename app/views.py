from django.shortcuts import render
from .models import Book
from .forms import FormBook

# Create your views here.
def base (request):
    return render(request,'base.html')

"""def add (request):
    if request.method=="POST":
        add_book=FormBook(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
    context={
      'form':FormBook()}
    return render(request,'add.html',context)"""

def calc (request):
    return render(request,'calc.html')

def home (request):
    context ={
        'book':Book.objects.all()
    }
    return render(request,'home.html',context)

from .forms import registerform
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import logout


def register (request):
    form=registerform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'register.html',{'form':form})

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def signin(request):
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')
    return render(request, 'login.html', {'form': form})



def logout_view(request):
       logout(request)
       return redirect('home') 

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormBook

@login_required
def add(request):
    if request.method == 'POST':
        form = FormBook(request.POST,request.FILES)
        if form.is_valid():
            maison = form.save(commit=False)
            maison.user = request.user
            maison.save()
            return redirect('home')  # Redirigez vers une vue listant les maisons
    else:
        form = FormBook()
    return render(request, 'add.html', {'form': form})