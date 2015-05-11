from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model, authenticate,login, logout

# Create your views here.
User=get_user_model()
def mylogin(request):
	form=LoginForm(request.POST or None)
	if form.is_valid():
		
		username_email=form.cleaned_data['username']
		password=form.cleaned_data['password']
		try:
			the_user=User.objects.get(username=username_email)
		except User.DoesNotExist:
			the_user=User.objects.get(email=username_email)
			
		except:
			the_user=None

		if the_user is not None:
			user=authenticate(username=the_user.username, password=password)
			
			if user.is_active:
				login(request,user)
				print("logged in")
				return HttpResponseRedirect('/admin/')
			else:
				print("inactive")
				#reactivate
		else:
			return HttpResponseRedirect('/register/')
			#Invalid account
	context={'form': form}
	return render(request,"form.html", context)

def register(request):
	form=RegisterForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data['username']
		email=form.cleaned_data['email']
		password=form.cleaned_data['password']
		new_user,created=User.objects.get_or_create(username=username,email=email)
		if created:
			new_user.password=password
			new_user.save()
	context={'form': form}
	return render(request,"form.html", context)
def mylogout(request):
	logout(request)
	return HttpResponseRedirect('/login/')
	return #sdf