from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from . import models

#forms for enquiry
class queryForm(forms.ModelForm):
    class Meta:
        model=models.Queries
        fields=('Name','email','description')

#form for new user registrations
class newUser(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username','password1','password2')

#form for update profile info
class updateProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username')

#for for trainerLogin 
class TrainerLoginForm(forms.ModelForm):
    class Meta:
        model =models.Trainer
        widgets = {
            "password": forms.PasswordInput(),
        }
        fields =("username", "password")


#form to  trainer profile detail
class TrainerProfileForm(forms.ModelForm):
	class Meta:
		model=models.Trainer
		fields=('full_name','mobile','address','detail','img')

#form for password change in trainer panel
class passwordChangeTrainer(forms.Form):
	new_password=forms.CharField(max_length=50,required=True)

#form for sending update to trainer 
class updateTrainerForm(forms.ModelForm):
	class Meta:
		model=models.userTrainerUpdate
		fields=('updateToTrainer','updateMsg')

#form for sending update to user
class updateUserForm(forms.ModelForm):

	class Meta:
		model=models.userTrainerUpdate
		fields=('updateToUser','updateMsg','updateFromTrainer')
		widgets={'updateFromTrainer': forms.HiddenInput()}

#form for update to both trainer and user
class updateTrainerForm(forms.ModelForm):
	
	class Meta:
		model=models.userTrainerUpdate
		fields=('updateToTrainer','updateMsg','updateFromUser')
		widgets={'updateFromUser': forms.HiddenInput()}
