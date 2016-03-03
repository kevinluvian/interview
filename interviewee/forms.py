from django import forms
from interviewer import models as interviewer_models

class GroupForm(forms.Form):
	groupcode = forms.CharField(max_length = 200)
	groupcode.widget = forms.TextInput(attrs = {'autofocus': 'autofocus',})

class DepartmentForm(forms.Form):
	def __init__(self, *args, **kwargs):
		groupcode = kwargs.pop('group')
		super(DepartmentForm, self).__init__(*args, **kwargs)
		#create a choice for groupcode selected
		self.fields['department'] = forms.ModelChoiceField(to_field_name="code", queryset = interviewer_models.InterviewDepartment.objects.filter(group__code__iexact = groupcode))
		self.fields['matric'] = forms.CharField(max_length = 200)
		self.fields['name'] = forms.CharField(max_length = 200)
		self.fields['year'] = forms.CharField(max_length = 200)
		self.fields['major'] = forms.CharField(max_length = 200)
		self.fields['phone'] = forms.CharField(max_length = 200)