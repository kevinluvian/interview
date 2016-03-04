from django.contrib import admin
from .models import Interviewee

class IntervieweeAdmin(admin.ModelAdmin):
	list_display = ['matric', 'get_group', 'get_department', 'name', 'year', 'major', 'phone', 'status', 'comment']
	def get_group(self, obj):
		return obj.group.name
	def get_department(self, obj):
		return obj.department.name
	get_department.short_description = 'Department'
	get_department.admin_order_field = 'department'
	get_group.short_description = 'Group'
	get_group.admin_order_field = 'group'

admin.site.register(Interviewee, IntervieweeAdmin)