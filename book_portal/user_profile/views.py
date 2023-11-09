from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import signUpForm
from django.contrib.auth import login

class LoginView(LoginView):
    template_name='account/login.html'

class SignUpView(View):
    def get(self, request):
        form = signUpForm()
        return render(request, 'account/signup.html', {'form': form})

    def post(self, request):
        form = signUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('get_books') 
        return render(request, 'account/signup.html', { 'form': form })