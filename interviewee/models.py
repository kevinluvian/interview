from django.db import models
from interviewer import models as interviewer_models


# Create your models here.
class Interviewee(models.Model):
	group = models.ForeignKey(interviewer_models.InterviewGroup)
	department = models.ForeignKey(interviewer_models.InterviewDepartment)
	queuenum = models.IntegerField(default = 0)
	matric = models.CharField(max_length = 200)
	name = models.CharField(max_length = 200)
	year = models.CharField(max_length = 200)
	major = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	status = models.IntegerField(default = 0)
	comment = models.TextField(blank = True)

	def __str__(self):
		return self.matric