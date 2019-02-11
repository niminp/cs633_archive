from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from manager.models import *
import manager.forms as forms

def main(request):
	return render(request, 'manager/project.html', {'projects': Project.objects.all()})

def login_user(request, errors=None):
	if errors is None:
		errors = []

	if request.user.is_authenticated:
		return redirect(request.GET.get('next', reverse("main")))

	if request.method == "POST":
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]

			user = authenticate(request, username=username , password=password)
			if user is not None and user.is_active:
				login(request, user)
				return redirect(request.GET.get('next', reverse("main")))
			else:
				errors.append("Invalid User Credentials")
		else:
			errors.append("Invalid Form Data")
	else:
		form = forms.LoginForm()

	return render(request, 'manager/login.html', {'login_form': form, 'errors': errors})

@login_required
def logout_user(request):
	logout(request)
	return redirect(reverse("main"))

@login_required
def upload(request):
	return render(request, 'manager/upload.html', {'projects': Project.objects.all()})