from django.contrib import admin
from .models import InterviewGroup, InterviewDepartment


class InterviewGroupAdmin(admin.ModelAdmin):
	list_display = ['name', 'code', 'lastqueue']

class InterviewDepartmentAdmin(admin.ModelAdmin):
	list_display = ['name', 'code', 'get_group', 'description', 'get_status', 'last_action']
	def get_group(self, obj):
		return obj.group.name
	def get_status(self, obj):
		if (obj.status == 0):
			return "break"
		elif (obj.status == 1):
			return "idling"
		elif (obj.status == 2):
			return ("calling queue number " + str(obj.status_desc))
		elif (obj.status == 3):
			return ("interviewing queue number " + str(obj.status_desc))
	get_status.short_description = 'status'
	get_group.short_description = 'Event'
	get_group.admin_order_field = 'code'

admin.site.register(InterviewGroup, InterviewGroupAdmin)
admin.site.register(InterviewDepartment, InterviewDepartmentAdmin)
