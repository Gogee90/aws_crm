from django import forms
from django.contrib.auth.models import User


class CreatEnvForm(forms.Form):
    #app_name = forms.CharField(max_length=50, label='ApplicationName')
    cname_prefix = forms.CharField(max_length=50, label='CNAMEPrefix')
    env_name = forms.CharField(max_length=50, label='EnvironmentName')
    #solution_stack = forms.CharField(max_length=100, label='SolutionStackName')


class CreateAppForm(forms.Form):
    app_name = forms.CharField(max_length=100, label='Application Name')
    description = forms.CharField(max_length=100, label='Description')


class UpdateAppForm(forms.Form):
    app_name = forms.CharField(max_length=100, label='Application Name')
    version_label = forms.CharField(max_length=30, label='Version label')


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password']