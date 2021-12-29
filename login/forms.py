from django import forms
from .models import Newproj
from .models import StudentsProfile


class NewprojForm(forms.ModelForm):

    class Meta:
        model = Newproj
        fields = ['Student_name', 'Username', 'Semester', 'Roll_no', 'Div', 'Project_name', 'Subject',
                  'Teacher_username', 'Project_description', 'Project_members', 'Git_link', 'Output_Image']

        widgets = {

            'Student_name': forms.TextInput(
                attrs={
                    'placeholder': 'Student Name',
                    'class': 'form-control'
                }
            ),
            'Username': forms.TextInput(
                attrs={
                    'placeholder': 'Student Username',
                    'class': 'form-control'
                }
            ),
            'Semester': forms.TextInput(
                attrs={
                    'placeholder': 'Semester',
                    'class': 'form-control'
                }
            ),
            'Roll_no': forms.TextInput(
                attrs={
                    'placeholder': 'Roll no.',
                    'class': 'form-control'
                }
            ),
            'Div': forms.TextInput(
                attrs={
                    'placeholder': 'Division',
                    'class': 'form-control'
                }
            ),
            'Project_name': forms.TextInput(
                attrs={
                    'placeholder': 'Project Name',
                    'class': 'form-control'
                }
            ),
            'Subject': forms.TextInput(
                attrs={
                    'placeholder': 'Subject',
                    'class': 'form-control'
                }
            ),
            'Teacher_username': forms.TextInput(
                attrs={
                    'placeholder': 'Teacher Username',
                    'class': 'form-control'
                }
            ),
            'Project_description': forms.Textarea(
                attrs={
                    'placeholder': 'Project Description',
                    'class': 'form-control'
                }
            ),
            'Project_members': forms.TextInput(
                attrs={
                    'placeholder': 'Tag your project members',
                    'class': 'form-control'
                }
            ),
            'Git_link': forms.TextInput(
                attrs={
                    'placeholder': 'Drop your git link',
                    'class': 'form-control'
                }
            )

        }


class StudentsProfileForm(forms.ModelForm):
    class Meta:
        model = StudentsProfile
        fields = [
            'project_score',
            'sem_average_marks',
            'test_score',
            'test_series_id',
            'language',
            'current_sem',
            'resume']
        widgets = {
            'project_score': forms.TextInput(
                attrs={
                    'placeholder': 'project_score',
                    'class': 'form-control'
                }
            ),
            'sem_average_marks': forms.TextInput(
                attrs={
                    'placeholder': 'sem_average_marks',
                    'class': 'form-control'
                }
            ),
            'test_score': forms.TextInput(
                attrs={
                    'placeholder': 'test_score',
                    'class': 'form-control'
                }
            ),
            'test_series_id': forms.TextInput(
                attrs={
                    'placeholder': 'test_series_id',
                    'class': 'form-control'
                }
            ),
            'language': forms.TextInput(
                attrs={
                    'placeholder': 'language',
                    'class': 'form-control'
                }
            ),
            'current_seme': forms.TextInput(
                attrs={
                    'placeholder': 'current_sem',
                    'class': 'form-control'
                }
            )

        }


class New_projForm(forms.Form):
    Student_name = forms.CharField(label='Your name', max_length=100)
