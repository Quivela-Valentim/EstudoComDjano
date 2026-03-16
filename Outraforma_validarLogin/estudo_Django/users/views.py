from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Loginform
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as authLogin

def login(request):
    
    error = False

    if request.method != 'POST':
        form = Loginform()
    
    else: 
        form= Loginform(data = request.POST)
        if form.is_valid():
            #username = request.POST.get('username')
            #password = request.POST.get('password')
            username = request.POST.get('login')
            password = request.POST.get('senha')
            user = authenticate(username = username, password= password)
            
            if user:
                authLogin(request, user )
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True
                
    context = {'form': form, 'error': error}
    return render(request, 'users/login.html', context)    
        

