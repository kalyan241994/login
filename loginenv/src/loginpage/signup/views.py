from django.shortcuts import render
from .forms import signupForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate



def signup(request):
	form=signupForm(request.POST or None)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=raw_password)
		login(request, user)
		return HttpResponse("<h1>You are succesfully registered</h1>")
	else:
		print(form.errors)
	return render(request,"signup.html",{"form":form})


# Create your views here.
