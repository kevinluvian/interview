from django.shortcuts import render, redirect
from django.http import HttpResponse
from interviewee.forms import GroupForm, DepartmentForm, QueueGroupForm
from interviewer import models as interviewer_models
from .models import Interviewee
from django.template.defaulttags import register
from django.http import JsonResponse

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

def queuegroup(request):
	form = QueueGroupForm()
	if (request.method == 'POST'):
		try :
			interviewer_models.InterviewGroup.objects.get(code = request.POST['groupcode'])
			return redirect(request.POST['groupcode'] + '/')
		except:
			return render(request, 'board/input3.html', {'form': form, 'status' : "wrong code"})
	return render(request, 'board/input3.html', {'form': form,})

def queueboard(request, group):
	return render(request, 'board/board.html')

def requestdata(request, group):
	deptlist = interviewer_models.InterviewDepartment.objects.filter(group__code = group).order_by('code')
	intervieweelist = Interviewee.objects.filter(group__code = group).order_by('queuenum')
	call = {}
	returndata = []
	maps = {}
	cnt = 0
	for w in deptlist :
		maps[w.code] = cnt
		cnt += 1
		returndata.append([])
		if (w.status == 0):
			returndata[-1].append("white")
		elif (w.status == 1):
			returndata[-1].append("yellow")
		elif (w.status == 2):
			returndata[-1].append("cyan")
		elif (w.status == 3):
			returndata[-1].append("red")
		returndata[-1].extend([w.code, w.name])
		call[w.code] = ""
	
	for w in intervieweelist:
		if (w.status == 0):
			if (len(returndata[maps[w.department.code]]) < 8):
				returndata[maps[w.department.code]].append(w.matric)
		elif (w.status == 1):
			call[w.department.code] = w.matric

	for w in returndata:
		while (len(w) < 8):
			w.append("")

	for key,val in call.items():
		returndata[maps[key]].append(val)

	return JsonResponse({'data' : returndata})