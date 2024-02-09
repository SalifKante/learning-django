from django import forms
from django.core import validators
from appOne.models import UserPractice
from django.contrib.auth.models import User
from appOne.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portofolio_site','profile_pic')
    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



"""def check_for_z(value):  
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")"""
    
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        vemail = all_cleaned_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure Emails Match")


    """
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher
    """

#Real Pratice

class UserPracticeForm(forms.ModelForm):
    class Meta:
        model = UserPractice
        fields = '__all__'