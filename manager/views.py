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

def project(request, project_id):
	errors = []

	try: 
		project = Project.objects.get(id=project_id)
	except: 
		errors.append("Invalid Project ID")


	return render(request, 'manager/project_view.html', {'project': project, 'errors': errors})

@login_required
def upload(request):

	if request.method == "GET":

		other_data = {
			'framework': Framework.objects.all(),
			'language': Language.objects.all(),
			'team_member': TeamMember.objects.all(),
			'keyword': Keyword.objects.all(),
		}

		form = forms.ProjectUpload()

		return render(request, 'manager/upload.html', {'projects': Project.objects.all(), 'project_form' : form,'other_data': other_data})

	elif request.method == 'POST':
		result = ""
		errors = []

		form = forms.ProjectUpload(request.POST, request.FILES)

		if form.is_valid():
			if len(form.errors) == 0:
				project = Project.objects.create(
					name = form.cleaned_data["name"],
					description = form.cleaned_data["description"],
					year = form.cleaned_data["year"],
					semester = form.cleaned_data["semester"],
					instructor = form.cleaned_data["instructor"],
					github = form.cleaned_data["github"],
					project_management = form.cleaned_data["project_management"],
					website = form.cleaned_data["website"],
					file = form.cleaned_data["file"],
					is_hidden = False,
				)

				project.facilitator.set(form.cleaned_data["facilitator"])

				team_member_list = form.cleaned_data["team_member"].split('|')
				team_member_list.remove("")
				team_member_queryset = []
				for x in team_member_list:
					team_member, created = TeamMember.objects.get_or_create(name=x)
					team_member_queryset.append(team_member)
				project.team_member.set(team_member_queryset)

				keyword_list = form.cleaned_data["keyword"].split('|')
				keyword_list.remove("")
				keyword_queryset = []
				for x in keyword_list:
					keyword, created = Keyword.objects.get_or_create(word=x)
					keyword_queryset.append(keyword)
				project.keyword.set(keyword_queryset)

				language_list = form.cleaned_data["language"].split('|')
				language_list.remove("")
				language_queryset = []
				for x in language_list:
					language, created = Language.objects.get_or_create(name=x)
					language_queryset.append(language)
				project.language.set(language_queryset)

				framework_list = form.cleaned_data["framework"].split('|')
				framework_list.remove("")
				framework_queryset = []
				for x in framework_list:
					framework, created = Framework.objects.get_or_create(name=x)
					framework_queryset.append(framework)
				project.framework.set(framework_queryset)
					
				project.save()

				return redirect(reverse('main'))

		if len(form.errors) > 0:
			errors.append("Please correct the below errors")

		return render(request, 'manager/upload.html', )
