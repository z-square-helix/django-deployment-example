from django import forms
from django.core import validators
from example_app.models import Userinos, UserProfileInfo
from django.contrib.auth.models import User

# CUSTOM VALIDATOR
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         rasie forms.ValidationError('Name does not start with Z')

class FormName(forms.Form):
#    name = forms.CharField(validators = [check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again')
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False, widget = forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])

    # CLEAN FUNCTION W/O USING BUILT IN
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT')

    # CLEAN THE ENTIRE FORM
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Emails do not match')

class SignUp(forms.ModelForm):

    class Meta:
        model = Userinos
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
