from django import forms
from django.contrib.auth.models import User
from manager.models import *

class LoginForm(forms.Form):
	username = forms.CharField(label="")
	username.widget.attrs.update({'class' : 'form-control m-1'})
	username.widget.attrs.update({'tabindex' : '1'})
	username.widget.attrs.update({'placeholder' : 'Username'})
	password = forms.CharField(widget=forms.PasswordInput, label="")
	password.widget.attrs.update({'class' : 'form-control m-1'})
	password.widget.attrs.update({'tabindex' : '2'})
	password.widget.attrs.update({'placeholder' : 'Password'})

class ProjectUpload(forms.Form):
	name = forms.CharField(label="Project Name*")
	name.widget.attrs.update({
		'class': 'form-control',
		'tabindex' : '1',
	})

	description = forms.CharField(widget=forms.Textarea, label="Description*")
	description.widget.attrs.update({
		'class': 'form-control',
		'tabindex' : '2',
	})

	year = forms.IntegerField(label="Year*")
	year.widget.attrs.update({
		'class': 'form-control',
		'min': 2000,
		'max': 3000,
		'tabindex' : '3',
	})

	semester = forms.ChoiceField(label="Semester*", choices=Project.SEMESTER_CHOICES)
	semester.widget.attrs.update({
		'class': 'form-control',
		'tabindex' : '4',
	})

	instructor = forms.ModelChoiceField(label="Instructor*", queryset=User.objects.filter(is_active = True, is_staff = True, is_superuser=False))
	instructor.widget.attrs.update({
		'class': 'form-control',
		'tabindex' : '5',
	})

	facilitator = forms.ModelMultipleChoiceField(label="Facilitator", queryset=User.objects.filter(is_active = True, is_staff = False, is_superuser=False), required=False)
	facilitator.widget.attrs.update({
		'class': 'form-control',
		'tabindex' : '6',
	})

	website = forms.CharField(label="Website Link", required=False)
	website.widget.attrs.update({
		'class': 'form-control',
		'tabindex' : '7',
	})

	github = forms.CharField(label="GitHub Link", required=False)
	github.widget.attrs.update({
		'class': 'form-control',
		'tabindex' : '8',
	})

	project_management = forms.CharField(label="Project Management Link", required=False)
	project_management.widget.attrs.update({
		'class': 'form-control',
		'tabindex' : '9',
	})

	file = forms.FileField(label='Select a file', required=False)
	file.widget.attrs.update({
		'tabindex' : '10',
	})

	framework = forms.CharField(widget = forms.HiddenInput(), required = False)
	language = forms.CharField(widget = forms.HiddenInput(), required = False)
	team_member = forms.CharField(widget = forms.HiddenInput(), required = False)
	keyword = forms.CharField(widget = forms.HiddenInput(), required = False)