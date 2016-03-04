from django.db import models
from datetime import datetime    

# Create your models here.
class InterviewGroup(models.Model):
	name = models.CharField(max_length = 200)
	code = models.CharField(max_length = 200, unique = True)
	lastqueue = models.IntegerField(default = 0)
	currentqueue = models.IntegerField(default = 0)
	def __str__(self):
		return self.code

class InterviewDepartment(models.Model):
	name = models.CharField(max_length = 200)
	code = models.CharField(max_length = 200, unique = True)
	group = models.ForeignKey(InterviewGroup)
	description = models.TextField()
	#0 = break , 1 = calling , 2 = interviewing , 3 = idle
	status = models.IntegerField(default = 0)
	status_desc = models.IntegerField(default = 0)
	last_action = models.DateTimeField(default = datetime.now)
	def __str__(self):
		return self.name
#	def waitedtime(self):
#		return (datetime.now() - last_action).total_seconds()

#	def statusnow(self):
#		if (status == 0):
#			return "break"
#		elif (status == 1):
#			return "idling"
#		elif (status == 2):
#			return ("calling queue number " . status_desc)
#		elif (status == 3):
#			return ("interviewing queue number " . status_desc)