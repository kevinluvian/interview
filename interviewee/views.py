from django.shortcuts import render, redirect
from django.http import HttpResponse
from interviewee.forms import GroupForm, DepartmentForm, QueueGroupForm
from interviewer import models as interviewer_models
from .models import Interviewee
from django.template.defaulttags import register

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
				tmp = Interviewee(group = group, department = dept, matric = request.POST['matric'], name = request.POST['name'], year = request.POST['year'], major = request.POST['major'], phone = request.POST['phone'], queuenum = (group.lastqueue + 1))
				group.lastqueue += 1
				group.save()
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

def queuegroup(request):
	form = QueueGroupForm()
	if (request.method == 'POST'):
		try :
			interviewer_models.InterviewGroup.objects.get(code = request.POST['groupcode'])
			return redirect(request.POST['groupcode'] + '/')
		except:
			return render(request, 'board/input3.html', {'form': form, 'status' : "wrong code"})
	return render(request, 'board/input3.html', {'form': form,})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def queueboard(request, group):
	deptlist = interviewer_models.InterviewDepartment.objects.filter(group__code = group)
	arr = {}
	alias = {}
	kosong = {}
	call = {}
	dept = []
	status = {}
	for w in deptlist :
		dept.append(w.code)
		alias[w.code] = w.name
		arr[w.code] = []
		status[w.code] = w.status
	intervieweelist = Interviewee.objects.filter(group__code = group).order_by('queuenum')
	for w in intervieweelist:
		if (w.status == 0):
			if (len(arr[w.department.code]) < 5):
				arr[w.department.code].append(w.queuenum)
		elif (w.status == 1):
			call[w.department.code] = w.queuenum
	for w in deptlist :
		kosong[w.code] = range(0,max(0,5-len(arr[w.code])))

	return render(request, 'board/board.html', {'status' : status, 'dept' : dept, 'alias' : alias, 'data' : arr, 'kosong' : kosong, 'calls' : call})