from django import forms
from .models import App,Report


class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['appName', 'text']
        labels = {'text': 'Opis Aplikacji', 'appName': 'Nazwa Aplikacji'}


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['text']
        labels = {}



