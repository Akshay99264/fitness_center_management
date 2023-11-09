from django.shortcuts import render,redirect
from django.core import serializers #using this we serialize our model data into json
from django.http import JsonResponse
from . import models
from . import forms

from datetime import timedelta
# Create your views here.
def home(request):
	slides=models.SlideShow.objects.all()
	offerings=models.ourOfferings.objects.all()[:3]
	eventimgs=models.EventImages.objects.all().order_by('-id')[:9]
	return render(request, 'home.html',{'slides':slides,'offerings':offerings,'eventimgs':eventimgs})

#PageDetail
def pDetail(request,id):
	page=models.Page.objects.get(id=id)
	return render(request, 'pInfo.html',{'page':page})

#FAQ
def commonQuestions(request):
	qna=models.Faq.objects.all()
	return render(request, 'common_queries.html',{'qnas':qna})

#Enquiry
def query(request):
    msg=''
    if request.method=='POST':
        q_form=forms.queryForm(request.POST)
        if q_form.is_valid():
            q_form.save()
            msg='Query has been sent'
    q_form=forms.queryForm
    return render(request, 'query.html',{'form':q_form,'msg':msg})


# showcase memories
def showcase(request):
	showcase=models.FunEvents.objects.all().order_by('-id')
	return render(request, 'showcase.html',{'events':showcase})

# display photos
def showcase_data(request,id):
	event=models.FunEvents.objects.get(id=id)
	event_imgs=models.EventImages.objects.filter(event=event).order_by('-id')
	return render(request, 'showcase_imgs.html',{'event_imgs':event_imgs,'event':event})

#Subscription Plans
def price(request):
	price=models.SubPlan.objects.all()
	dfeatures=models.SubPlanFeature.objects.distinct('title')
	return render(request, 'costs.html',{'plans':price,'dfeatures':dfeatures})

def newUser(request):
	msg=None
	if request.method=='POST':
		newForm=forms.newUser(request.POST)
		if newForm.is_valid():
			newForm.save()
			msg='Thank you for register.'
	newForm=forms.newUser
	return render(request, 'registration/newUser.html',{'form':newForm,'msg':msg})


# User Dashboard implementation starts here
def user_dashboard(request):
	my_trainer=models.AssignSubscriber.objects.get(user=request.user)
	current_plan=models.Members.objects.get(user=request.user)
	enddate=current_plan.register_date+timedelta(days=current_plan.plan.validity_days)

	# Notification
	data=models.Notify.objects.all().order_by('-id')
	notifStatus=False
	jsonData=[]
	totalUnread=0
	for d in data:
		try:
			notifStatusData=models.NotifUserStatus.objects.filter(user=request.user,notif=d).first()
			if notifStatusData:
				notifStatus=True
		except models.NotifUserStatus.DoesNotExist:
			notifStatus=False
		if not notifStatus:
			totalUnread=totalUnread+1

	return render(request, 'user/dashboard.html',{
		'current_plan':current_plan,
		'my_trainer':my_trainer,
		'total_unread':totalUnread,
		'enddate':enddate
	})


# Edit form
def update_profile(request):
	msg=None
	if request.method=='POST':
		form=forms.ProfileForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			msg='Data has been saved'
	form=forms.ProfileForm(instance=request.user)
	return render(request, 'user/update-profile.html',{'form':form,'msg':msg})

def trainerlogin(request):
	msg=''
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		trainer=models.Trainer.objects.filter(username=username,password=password).count()
		if trainer > 0:
			trainer=models.Trainer.objects.filter(username=username,password=password).first()
			request.session['trainerLogin']=True
			request.session['trainerid']=trainer.id
			return redirect('/trainer_dashboard')
		else:
			msg='Invalid Credentials!!'
	form=forms.TrainerLoginForm
	return render(request, 'trainer/trainer_login.html',{'form':form,'msg':msg})

# TrainerLogout
def trainerlogout(request):
	del request.session['trainerLogin']
	return redirect('/trainerlogin')

# Trainer Dashboard
def trainer_dashboard(request):
	return render(request,'trainer/trainer_dashboard.html')

# Trainer Profile
def trainer_profile(request):
	t_id=request.session['trainerid']
	trainer=models.Trainer.objects.get(pk=t_id)
	msg=None
	if request.method=='POST':
		form=forms.TrainerProfileForm(request.POST,request.FILES,instance=trainer)
		if form.is_valid():
			form.save()
			msg='Profile has been updated'
	form=forms.TrainerProfileForm(instance=trainer)
	return render(request, 'trainer/profile.html',{'form':form,'msg':msg})

#Notifications
def notification(request):
	data=models.Notify.objects.all().order_by('-id')
	return render(request,'notification.html',{'data':data})

#get All Notifications
def get_notification(request):
	data=models.Notify.objects.all().order_by('-id')
	notifStatus=False
	jsonData=[]
	totalUnread=0
	for d in data:
		try:
			notifStatusData=models.NotifUserStatus.objects.filter(user=request.user,notif=d).first()
			if notifStatusData:
				notifStatus=True
		except models.NotifUserStatus.DoesNotExist:
			notifStatus=False
		if not notifStatus:
			totalUnread=totalUnread+1
		jsonData.append({
				'pk':d.id,
				'notify_detail':d.notify_detail,
				'notifStatus':notifStatus
			})
	# jsonData=serializers.serialize('json', data)
	return JsonResponse({'data':jsonData,'totalUnread':totalUnread})

# Mark Read By user
def mark_read_notif(request):
	notif=request.GET['notif']
	notif=models.Notify.objects.get(pk=notif)
	user=request.user
	models.NotifUserStatus.objects.create(notif=notif,user=user,status=True)
	return JsonResponse({'bool':True})

# Trainer Subscribers
def trainer_subscribers(request):
	trainer=models.Trainer.objects.get(pk=request.session['trainerid'])
	trainer_subs=models.AssignSubscriber.objects.filter(trainer=trainer).order_by('-id')
	return render(request,'trainer/trainer_subscribers.html',{'trainer_subs':trainer_subs})

# Trainer Payments
def trainer_payments(request):
	trainer=models.Trainer.objects.get(pk=request.session['trainerid'])
	trainer_pays=models.TrainerSalary.objects.filter(trainer=trainer).order_by('-id')
	return render(request, 'trainer/trainer_payments.html',{'trainer_pays':trainer_pays})


# Trainer Notification
def trainer_notifications(request):
	data=models.TrainerNotification.objects.all().order_by('-id')
	return render(request,'trainer/notification.html',{'notifs':data})


# password change trainer
def passwordChange_trainer(request):
	msg=None
	if request.method=='POST':
		new_password=request.POST['new_password']
		updateRes=models.Trainer.objects.filter(pk=request.session['trainerid']).update(password=new_password)
		if updateRes:
			del request.session['trainerLogin']
			return redirect('/trainerlogin')
		else:
			msg='Error while changing password'
	form=forms.passwordChangeTrainer
	return render(request, 'trainer/chagePassword_trainer.html',{'form':form})


# Trainer Messages
def trainer_msgs(request):
	data=models.TrainerMsg.objects.all().order_by('-id')
	return render(request, 'trainer/msgs.html',{'msgs':data})
