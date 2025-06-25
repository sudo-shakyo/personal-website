from ast import For
from django.views.generic import ListView
import requests
from social_django.models import UserSocialAuth
from flask import Flask, render_template, request
from django.shortcuts import render


from django.shortcuts import render
from django.http import JsonResponse
from blog.models import Query, ConsumerHelpDatabase
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from codewithshakyo.forms import SignUpForm, EditProfileForm 
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views.generic import CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from blog.models import Contact, Msg
from datetime import datetime
from blog.models import Search
import webbrowser
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'testing.html'




def about(request):
	return render(request, 'blog.html')

def announcements(request):
    return render(request, 'announcements.html')


def homepage(request):
    return render(request, 'home.html')


			



def jarvis(request):
	return render(request, 'jarvis.html')




def blog(request):
	return render(request, 'blog.html')
def message(request):
	if request.method == 'POST':
		name1=request.POST.get('name1')
		#email1=request.POST.get('email1')
		msg=request.POST.get('msg')
		message=Msg(name1=name1, #email1=email1, 
		msg=msg, date1=datetime.today())
		message.save()
	return render(request, 'home.html')
 
def home(request):
    return render(request, 'home.html')

def index(request): 
	return render(request, 'index.html', {})

def help(request):
	return render(request, 'chat-help.html')

	


def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Youre logged in'))
			return render(request, 'index.html') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return render(request,'login.html') #re routes to login page upon unsucessful login
	else:
		return render(request, 'login.html')
		
@login_required
def personal_info(request):
	return render(request, 'index.html')



@login_required
def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return render(request, 'login.html')

def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Youre now registered'))
			return render(request, 'index.html')
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'register.html', context)

@login_required
def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile'))
			return render(request,'index.html')
	else: 		#passes in user information 
		form = EditProfileForm(instance= request.user) 

	context = {'form': form}
	return render(request, 'edit_profile.html', context)
	#return render(request, 'authenticate/edit_profile.html',{})


@login_required
def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return render(request,'index.html')
	else: 		#passes in user information 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'change_password.html', context)
    
def login_testing(request):
	return render(request, 'login_testing.html')


def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		username = request.POST.get('username')
		desc = request.POST.get('desc')
		contact = Contact(name=name, desc=desc, email=email, username=username ,date=datetime.now())
		contact.save()
	return render(request, 'contact.html')

def terms(requests):
	return HttpResponse("Terms and Conditions Page Conditions: \n 1. If you use my website then you are not supposed to copy paste my code in your website.\n 2. If you copy paste my code then it is your reponsibility to ensure that it works properly it is not my fault if the code doesn't run at your server. \n 3. I am no way responsible if your password or account in this website gets hacked. \n 4. You may or may not get the reply of your message that you have posted in the contact page. \n 5. If you login in my website then it is your sole duty to remember your password. \n 5.1. If you still forget your password then you can go to the forgot password page and raise a complaint. But you may or may not get your new password and if you get it and you don't like the passoword then you can change it at the change password page. \n 6. You shall not post any rude or hate message at the contact page and if you do then your account might be terminated. ")


def sitemap(requests):
	return render(requests,"sitemap.txt")



class SettingsView(LoginRequiredMixin, TemplateView):
	def get(self, request, *args, **kwargs):
		user =  request.user

		try:
			github_login = user.social_auth.get(provider = 'github')
		except UserSocialAuth.DoesNotExist:
			github_login = None
		
		try:
			twitter_login = user.social_auth.get(provider = 'twitter')
		except UserSocialAuth.DoesNotExist:
			twitter_login = None
		
		try:
			facebook_login = user.social_auth.get(provider = 'facebook')
		except UserSocialAuth.DoesNotExist:
			facebook_login = None

		can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

		return render(request, 'index.html',{
			'github_login' : github_login,
			'twitter_login' : twitter_login,
			'facebook_login' : facebook_login,
			'can_disconnect' : can_disconnect
		})
	


data = [
    ('How do I reset my password?', 'You can reset your password by going to the account settings page.'),
    ('How do I cancel my subscription?', 'To cancel your subscription, go to the subscription page and click on the cancel button.'),
    ('What payment methods do you accept?', 'We accept credit cards, PayPal, and Apple Pay.'),
    ('How do I contact customer support?', 'You can contact customer support by emailing support@example.com or calling our toll-free number.'),
]




def testimonials(request):
	return render(request, 'testimonials.html')