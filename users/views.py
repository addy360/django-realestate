from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact

def login(request):
	if request.method =="POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is None:
			messages.error(request,'wrong username or password')
			return redirect('login')
		else:
			auth.login(request,user)
			return redirect('dashboard')	
	else:		
		return render(request, 'users/login.html')


def register(request):
	if request.method == 'POST':
		# getting form values
		firstname = request.POST['first_name']
		lastname = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		password2 = request.POST['password2']

		if password!=password2:
			messages.error(request,'passwords do not match')
			return redirect('register')
		elif User.objects.all().filter(username=username).exists():
			messages.error(request,'Username is already taken')
			return redirect('register')	
		elif User.objects.all().filter(email=email).exists():
			messages.error(request,'Email is already taken')
			return redirect('register')	
		else:
			User.objects.create_user(first_name=firstname, last_name=lastname, email=email,username=username, password=password).save() 
			messages.success(request,'You have been registered successfully and can now login')	
			return redirect('login')
	else:		
		return render(request, 'users/register.html')

def logout(request):
	if request.method=="POST":
		auth.logout(request)
		return redirect('index')

def dashboard(request):
	contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
	context = {
		'contacts': contacts
	}
	return render(request, 'users/dashboard.html',context)	