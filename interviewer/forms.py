from django import forms
from interviewee.models import Interviewee as interviewee_models
from django.utils import html

class SubmitButtonWidget(forms.Widget):
    def render(self, name, value, attrs = None):
        return '<input type="submit" name="%s" value="%s">' % (html.escape(name), html.escape(value))


class SubmitButtonField(forms.Field):
    def __init__(self, *args, **kwargs):
        if not kwargs:
            kwargs = {}
        kwargs["widget"] = SubmitButtonWidget

        super(SubmitButtonField, self).__init__(*args, **kwargs)

    def clean(self, value):
        return value

class LoginForm(forms.Form):
	code = forms.CharField(max_length = 200)
	code.widget = forms.TextInput(attrs = {'autofocus' : 'autofocus',})

class InterviewForm(forms.Form):
	def __init__(self, *args, **kwargs):
		queuenum = kwargs.pop('queuenum')
		code = kwargs.pop('code')
		super(InterviewForm, self).__init__(*args, **kwargs)
		#create a choice for groupcode selected
		self.fields['comment'] = forms.CharField(max_length = 200, initial = interviewee_models.objects.get(department__code = code, queuenum = queuenum).comment)
		self.fields['score'] = forms.IntegerField(initial = interviewee_models.objects.get(department__code = code, queuenum = queuenum).score)

class CallingForm(forms.Form):
	def __init__(self, *args, **kwargs):
		queuenum = kwargs.pop('queuenum')
		super(CallingForm, self).__init__(*args, **kwargs)
		self.fields['queuenum'] = forms.IntegerField(widget = forms.HiddenInput(), initial = queuenum)
	startinterview = SubmitButtonField(label = "", initial = "Start Interview")
	cancelcall = SubmitButtonField(label = "", initial = "Put back to queue")
	absent = SubmitButtonField(label = "", initial = "Mark as Absent")
