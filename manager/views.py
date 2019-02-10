from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from manager.models import *

def main(request):

	return render(request, 'manager/project.html', {'projects': Project.objects.all()})