from django import forms
from apps.api.heroes.models import Application

class ApplicationAdminForm(forms.ModelForm):
    approve = forms.BooleanField(required=False)
    reject = forms.BooleanField(required=False)

    class Meta:
        model = Application
        fields = '__all__'
