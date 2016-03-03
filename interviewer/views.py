from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import InterviewDepartment
from django.http import JsonResponse
from interviewee.models import Interviewee as interviewee_models

def login(request):
	if (request.method == 'POST'):
		try:
			q = InterviewDepartment.objects.get(code = request.POST['code'])
		except:
			form = LoginForm()
			return render(request, 'login/input.html', {'form': form, 'status' : "wrong code"})

		return redirect(request.POST['code'] + '/')
	else:
		form = LoginForm()
		return render(request, 'login/input.html', {'form': form,})

def queuelist(request, code):
	requestmatric = {}
	arrmatric = []
	ret = ""
	for e in interviewee_models.objects.filter(department__code = code).order_by('queuenum'):
		queuestudent = []
		queuestudent.append(e.queuenum)
		queuestudent.append(e.matric)

		arrmatric.append(queuestudent)
	requestmatric['data'] = arrmatric
	return JsonResponse(requestmatric)

#	return HttpResponse('Hello, world. Youre at the choose department index. ' + code)