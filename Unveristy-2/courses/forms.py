from django import forms
from .models import Teacher, Subject


class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=200)
    code = forms.CharField(max_length=200)
    start_data = forms.DateField()
    is_activate = forms.BooleanField()


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['frist_name', 'last_name', 'degree']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'specialities', 'teachers']
