from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label="")
	username.widget.attrs.update({'class' : 'form-control m-1'})
	username.widget.attrs.update({'tabindex' : '1'})
	username.widget.attrs.update({'placeholder' : 'Username'})
	password = forms.CharField(widget=forms.PasswordInput, label="")
	password.widget.attrs.update({'class' : 'form-control m-1'})
	password.widget.attrs.update({'tabindex' : '2'})
	password.widget.attrs.update({'placeholder' : 'Password'})