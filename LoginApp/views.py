from django.shortcuts import render
from django.http import HttpResponse
from LoginApp.models import Register
from LoginApp.forms import RegistrationForm,RegistrationModelForm
# Create your views here.


def index(request):
	#print request.session['sessonId'] = 'abc'
	#request.COOKIES[]
	#request.session.has_key('sessionId')
	#print request.session.get('sessionId')
	#request.session.flush()
	return render(request,'LoginApp/index.html')

def register(request):
	return render(request,'LoginApp/register.html')
def login(request):
	return render(request,'LoginApp/login.html')



def register_success(request):
	print request.method
	if request.method == 'POST':
		print request.POST
		name = request.POST['uname']
		password = request.POST['pwd']
		email = request.POST['email']
		gender = request.POST['gender']
		try:
			obj = Register(name=name,password=password,email = email,gender=gender)
			obj.save()
		except Exception as e:
			return render(request,'LoginApp/exception.html',{'exception':e})
		return render(request,'LoginApp/register_success.html',{'uname':name,'email':email})

	else:
		print 'else'
		return render(request,'LoginApp/register.html')


def login_success(request):
	print 'hai'
	if request.method == 'POST':
		name=request.POST['uname']
		pwd=request.POST['pwd']
		#obj=Register.objects.get(name=name,password=pwd)
		try:
			obj = Register.objects.get(name=name)
			if pwd == obj.password:
				return render(request,'LoginApp/login_success.html',{'uname':name})
			else:
				return HttpResponse('Invalid Username/password')
		except Exception as e:
			return render(request,'LoginApp/exception.html',{'exception':e})

	else:
		print 'invalid username'
		return render(request,'LoginApp/register.html')






def register_form(request):
	#form = RegistrationForm()
	form = RegistrationModelForm()
	return render(request,'LoginApp/register_form.html',{'form':form})



def register_success_form(request):
	if request.method == 'POST':
		#form = RegistrationForm(request.POST)
		form = RegistrationModelForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['uname']
			password = form.cleaned_data['pwd']
			email = form.cleaned_data['email']
			gender = form.cleaned_data['gender']
			try:
				obj = Register(name=name,password=password,email = email,gender=gender)
				obj.save()
			except Exception as e:
				return render(request,'LoginApp/exception.html',{'exception':e})
			return render(request,'LoginApp/register_success.html',{'uname':name,'email':email})
		else:
			return render(request,'LoginApp/register_form.html',{'form':form})

	else:
		print 'else'
		return render(request,'LoginApp/register.html')