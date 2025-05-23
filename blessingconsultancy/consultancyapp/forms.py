from django import forms

from .models import ContactForm,careerApplication

class contact(forms.ModelForm):
    class Meta:
        model =  ContactForm
        fields = ['name','age','email','mobile','qualification','experience','address']


class careerApplicationform(forms.ModelForm):
    class Meta:
        model = careerApplication
        fields = ['fullname','email','phone','position','resume']