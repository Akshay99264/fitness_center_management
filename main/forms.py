from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from . import models

class queryForm(forms.ModelForm):
    class Meta:
        model=models.Queries
        fields=('Name','email','description')

class newUser(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2')

class ProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username')

class TrainerLoginForm(forms.ModelForm):
    class Meta:
        model =models.Trainer
        widgets = {
            "password": forms.PasswordInput(),
        }
        fields =("username", "password")

class TrainerProfileForm(forms.ModelForm):
	class Meta:
		model=models.Trainer
		fields=('full_name','mobile','address','detail','img')


class passwordChangeTrainer(forms.Form):
	new_password=forms.CharField(max_length=50,required=True)

class updateTrainerForm(forms.ModelForm):
	class Meta:
		model=models.userTrainerUpdate
		fields=('updateToTrainer','updateMsg')

class updateUserForm(forms.ModelForm):
	class Meta:
		model=models.userTrainerUpdate
		fields=('updateToUser','updateMsg','updateFromTrainer')
		widgets={'updateFromTrainer': forms.HiddenInput()}

class updateTrainerForm(forms.ModelForm):
	class Meta:
		model=models.userTrainerUpdate
		fields=('updateToTrainer','updateMsg','updateFromUser')
		widgets={'updateFromUser': forms.HiddenInput()}
