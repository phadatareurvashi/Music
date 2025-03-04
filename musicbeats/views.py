
from django.shortcuts import render,redirect
from musicbeats.models import song
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import song 


def index(request):
    songs = song.objects.all()
    return render(request,'index.html',{'songs':songs})

def login(request):
    # Your login logic here
    return render(request, 'login.html')

def signup(request):
    # Your signup logic here
    return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')  # Redirect to a success page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or home page
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup_success(request):
    return render(request, 'signup_success.html')
# Create your views here.

def songs(request):
    songs = song.objects.all()
    return render(request,'musicbeats/songs.html',{'songs':songs})

def songpost(request,id):
    songs = song.objects.filter(song_id=id).first()
    return render(request,'musicbeats/songpost.html',{'songs':songs})

