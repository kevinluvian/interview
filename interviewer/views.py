from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, CallingForm, InterviewForm
from .models import InterviewDepartment
from django.http import JsonResponse
from interviewee.models import Interviewee as interviewee_models
from datetime import datetime

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
	w = InterviewDepartment.objects.get(code = code)
	if (request.method == 'POST'):
		if (w.status == 1):
			try:
				if (request.POST['startinterview'] == "Start Interview"):
					q = interviewee_models.objects.get(queuenum = request.POST['queuenum'], department__code = code)
					w.status = 2
					q.status = 2
					w.last_action = datetime.now()
					q.last_action = datetime.now()
					w.save()
					q.save()
	#				form = InterviewForm(queuenum = request.POST['queuenum'])
	#				return render(request, 'queuelist/interview.html', {'form' : form, 'queuenum' : request.POST['queuenum'],})
			except:
				pass

			try:
				if (request.POST['absent'] == "Mark as Absent"):
					q = interviewee_models.objects.get(queuenum = request.POST['queuenum'], department__code = code)
					w.status = 0
					q.status = 3
					w.last_action = datetime.now()
					q.last_action = datetime.now()
					w.save()
					q.save()
			except:
				pass

			try:
				if (request.POST['cancelcall'] == "Put back to queue"):
					q = interviewee_models.objects.get(queuenum = request.POST['queuenum'], department__code = code)
					w.status = 0
					q.status = 0
					w.last_action = datetime.now()
					q.last_action = datetime.now()
					w.save()
					q.save()
			except:
				pass

		elif (w.status == 2):
			#update interviewee punya status sama score, trus status interviewee dan interviewer
			q = interviewee_models.objects.get(queuenum = w.status_desc, department__code = code)
			w.status = 0
			q.status = 3
			w.last_action = datetime.now()
			q.last_action = datetime.now()
			try:
				q.score = request.POST['score']
			except:
				q.score = 0
			try:
				q.comment = request.POST['comment']
			except:
				q.comment = ""
			q.save()
			w.save()

	if (w.status == 1):
		form = CallingForm(queuenum = w.status_desc)
		return render(request, 'queuelist/call.html', {'form' : form, 'queuenum' : w.status_desc, 'last_action' : w.last_action})
	elif(w.status == 2):
	#	return HttpResponse('wstatus 2 ' + str(w.status_desc))
		form = InterviewForm(queuenum = w.status_desc, code = w.code)
		studentinfo = interviewee_models.objects.get(department__code = code, queuenum = w.status_desc)
		return render(request, 'queuelist/interview.html', {'form' : form, 'studentinfo' : studentinfo, 'queuenum' : w.status_desc,})

	pendingstudent = []
	finishedstudent = []
	ret = ""
	for e in interviewee_models.objects.filter(department__code = code).order_by('queuenum'):
		queuestudent = []
		queuestudent.append(e.queuenum)
		queuestudent.append(e.matric)
		if (e.status == 0):
			pendingstudent.append(queuestudent)
		elif (e.status == 3):
			queuestudent.append(e.comment)
			queuestudent.append(e.score)
			finishedstudent.append(queuestudent)
	return render(request, 'queuelist/index.html', {'pending' : pendingstudent, 'finished' : finishedstudent,})

#	requestmatric['data'] = arrmatric
#	return JsonResponse(requestmatric)

#	return HttpResponse('Hello, world. Youre at the choose department index. ')

def call(request, code, queuenum):
	w = InterviewDepartment.objects.get(code = code)
	if (w.status == 0):
		#update interviewee statusnya,
		q = interviewee_models.objects.get(queuenum = queuenum, department__code = code)
		q.status = 1
		w.status = 1
		w.status_desc = queuenum
		w.last_action = datetime.now()
		q.last_action = datetime.now()
		w.save()
		q.save()
	return redirect("../..")
	#update interviewer statusnya

def delete(request, code, queuenum):
	q = interviewee_models.objects.get(queuenum = queuenum, department__code = code)
	q.delete()
	return redirect("../..")