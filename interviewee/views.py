from django.shortcuts import render, redirect
from django.http import HttpResponse
from interviewee.forms import GroupForm, DepartmentForm
from interviewer import models as interviewer_models
from .models import Interviewee

def group(request):
	form = GroupForm()
	ret = ""
	if (request.method == 'POST'):
		try:
			dept = request.POST['department']
		except:
			try:
				group = request.POST['groupcode']
				interviewer_models.InterviewGroup.objects.get(code = group)
			except:
				return render(request, 'register/input.html', {'form': form, 'status' : "wrong code",})

			return redirect(group + '/')
		
		dept = interviewer_models.InterviewDepartment.objects.get(code = dept)
		group = dept.group

		if (DepartmentForm(request.POST, group = group).is_valid()):
			try:
				tmp = Interviewee(group = group, department = dept, matric = request.POST['matric'], name = request.POST['name'], year = request.POST['year'], major = request.POST['major'], phone = request.POST['phone'])
				tmp.save()
			except:
				return render(request, 'register/input.html', {'form': form, 'status' : "form not valid",})
			else:
				return render(request, 'register/input.html', {'form': form, 'status' : "success",})
		else:
			return render(request, 'register/input.html', {'form': form, 'status' : "form not valid",})

	return render(request, 'register/input.html', {'form': form, 'status' : ret,})

def department(request, group):
	form = DepartmentForm(group = group)
	return render(request, 'register/input2.html', {'form': form,})
#	return HttpResponse('Hello, world. Youre at the choose department index. ' + group)