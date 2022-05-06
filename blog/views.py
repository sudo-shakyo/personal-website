from ast import For

from django.views.generic import ListView
import requests
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from codewithshakyo.forms import SignUpForm, EditProfileForm 
# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from blog.models import Contact, Msg
from datetime import datetime
from blog.models import Search
import webbrowser
#from motech.mars import call


# Create your views here.
'''
def cam():
        key = cv2.waitKey(1)
        webcam= cv2.VideoCapture(0)
        while True:
         try:
                check, frame= webcam.read()
                print(check)
                print(frame)
                cv2.imshow("capturing", frame)
                key= cv2.waitKey(1)
                if key == ord('s'):
                    cv2.imwrite(filename="saved_img.jpg", img=frame)
                    webcam.release()
                    img_new= cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                    img_new= cv2.imshow("Captured Image", img_new)
                    cv2.waitKey(1650)
                    cv2.destroyAllWindows()
                    print("processing image")
                    img_=cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                    gray=cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                    img_=cv2.resize(gray,(28,29))
                    img_resized=cv2.imwrite(filename='saved_img_final.jpg', img=img_)
                    print("image saved! ")
                    break
                elif key == ord('q'):
                    print("turning off camera")
                    webcam.release()
                    print("program ended")
                    cv2.destroyAllWindows()
                    break
         except(KeyboardInterrupt):
                print("turning off camera")
                webcam.release()
                print("camera is off")
                cv2.destroyAllWindows()
                break
'''
def about(request):
	return render(request, 'blog.html')

def announcements(request):
    return render(request, 'announcements.html')


def homepage(request):
    return render(request, 'home.html')


			
 






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
    

'''
def contact(request):
    if request.method== 'POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        desc=request.POST['desc']
        #contact= Contact(name=name, desc=desc, email=email, username=username, date=datetime.today())
        #contact.save()
		send_mail(
			name, # subject 
			desc, # message
			email, # from email
			['officialshakyo@gmail.com'])
		return render(request, 'contact.html')
'''


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
	return HttpResponse("Terms and Conditions Page Conditions: \n 1. If you use my website then you are not supposed to copy paste my code in your website.\n 2. If you copy paste my code then it is your reponsibility to ensure that it works properly it is not my fault if the code doesn't run at your server. \n 3. I am no way responsible if your password or account in this website gets hacked. \n 4. You may or may not get the reply of your message that you have posted in the contact page. \n 5. If you login in my website then it is your sole duty to remember your password. \n 5.1. If you still forget your password then you can go to the forgot password page and raise a complaint. But you may or may not get your new password and if you get it and you don't like the passoword then you can change it at the change password page. \n 6. You shall not post any rude or hate message at the contact page and if you do then your account might be terminated.")
def sitemap(requests):
	return render(requests,"sitemap.txt")