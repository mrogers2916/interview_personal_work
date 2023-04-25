from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method =='POST':
        print("I am here1")
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

        user = LoginAuthBackened().authenticate(request=request, username=username, password=password)
        if user:
            messages.success(request, f'Login Successful.')
            return redirect('app-workspace')
        else:
            messages.error(request, f'Password Incorrect !')
            return redirect('app-login')
    else:
        print(form.errors)
else:
    form = LoginForm()
return render(request, 'users/login.html', {'form': form})

from django.contrib.auth import authenticate, login
# After check autentication
user = authenticate(username=username, password=password)

print(user.is_authenticated, request.user.is_authenticated)

# you must login request
if user and  user.is_active:
    login(request, user)
print(user.is_authenticated, request.user.is_authenticated)