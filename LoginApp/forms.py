from django import forms
from LoginApp.models import Register


class RegistrationForm(forms.Form):
	uname = forms.CharField(max_length = 255)
	pwd = forms.CharField(max_length=255,widget=forms.PasswordInput)
	email  = forms.EmailField(max_length = 255,required = False)
	gender = forms.ChoiceField(choices = (('male','male'),('female','female')),widget=forms.RadioSelect)
	#gender1 = forms.BooleanField()



class RegistrationModelForm(forms.ModelForm):
 	
 	class Meta:
 		model = Register
 		fields = '__all__'	#('name','password')
