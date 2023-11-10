from django.shortcuts import render,redirect
from django.core import serializers #using this we serialize our model data into json
from django.http import JsonResponse
from . import models
from . import forms

from datetime import timedelta
def home(request):
	slides=models.SlideShow.objects.all()
	offerings=models.ourOfferings.objects.all()[:3]
	eventimgs=models.EventImages.objects.all().order_by('-id')[:9]
	return render(request, 'home.html',{'slides':slides,'offerings':offerings,'eventimgs':eventimgs})

# view for PageDetail
def pDetail(request,id):
	page=models.Page.objects.get(id=id)
	return render(request, 'pInfo.html',{'page':page})

# view for Frequently asked questions
def commonQuestions(request):
	qna=models.Faq.objects.all()
	return render(request, 'common_queries.html',{'qnas':qna})

# view for query
def query(request):
    msg=''
    if request.method=='POST':
        q_form=forms.queryForm(request.POST)
        if q_form.is_valid():
            q_form.save()
            msg='Query has been sent'
    q_form=forms.queryForm
    return render(request, 'query.html',{'form':q_form,'msg':msg})


# view for showcase memories
def showcase(request):
	showcase=models.FunEvents.objects.all().order_by('-id')
	return render(request, 'showcase.html',{'events':showcase})

# view for display photos
def showcase_data(request,id):
	event=models.FunEvents.objects.get(id=id)
	event_imgs=models.EventImages.objects.filter(event=event).order_by('-id')
	return render(request, 'showcase_imgs.html',{'event_imgs':event_imgs,'event':event})

# view for Subscription Plans
def cost(request):
	cost=models.SubPlan.objects.all()
	amenities=models.SubPlanFeature.objects.distinct('title')
	return render(request, 'costs.html',{'plans':cost,'dfeatures':amenities})

def newUser(request):
	msg=None
	if request.method=='POST':
		newForm=forms.newUser(request.POST)
		if newForm.is_valid():
			newForm.save()
			msg='Thank you for register.'
	newForm=forms.newUser
	return render(request, 'registration/newUser.html',{'form':newForm,'msg':msg})


# view for  User Dashboard implementation starts here
def user_dashboard(request):
	allocatedTrainer=models.AssignSubscriber.objects.get(user=request.user)
	subscribedPlan=models.Members.objects.get(user=request.user)
	expiryDate=subscribedPlan.register_date+timedelta(days=subscribedPlan.plan.validity_days)

	# for  Notification
	notificationData=models.Notifications.objects.all().order_by('-id')
	notificationStatus=False
	jsonData=[]
	totalUnread=0
	for data in notificationData:
		try:
			notificationStatusData=models.NotifUserStatus.objects.filter(user=request.user,notif=data).first()
			if notificationStatusData:
				notificationStatus=True
		except models.NotifUserStatus.DoesNotExist:
			notificationStatus=False
		if not notificationStatus:
			totalUnread=totalUnread+1

	return render(request, 'user/dashboard.html',{
		'subscribedPlan':subscribedPlan, 
		'allocatedTrainer':allocatedTrainer,
		'total_unread':totalUnread,
		'expiryDate':expiryDate
	})

# view for user messages
def user_msgs(request):
	data=models.UserMsg.objects.all().order_by('-id')
	return render(request, 'user/messages.html',{'msgs':data})


# view for  Edit form
def modify_profileData(request):
	message=None
	if request.method=='POST':
		profileForm=forms.updateProfileForm(request.POST,instance=request.user)
		if profileForm.is_valid():
			profileForm.save()
			message='Data has been saved'
	profileForm=forms.updateProfileForm(instance=request.user)
	return render(request, 'user/modifyProfileData.html',{'profileForm':profileForm,'message':message})

# view for trainer login page
def trainerlogin(request):
	message=''
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
			message='Invalid Credentials!!'
	form=forms.TrainerLoginForm
	return render(request, 'trainer/trainer_login.html',{'form':form,'message':message})

# view for  TrainerLogout
def trainerlogout(request):
	del request.session['trainerLogin']
	return redirect('/trainerlogin')

# view for  Trainer Dashboard
def trainer_dashboard(request):
	return render(request,'trainer/trainer_dashboard.html')

# view for  Trainer Profile
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
	return render(request, 'trainer/update_profileData.html',{'form':form,'msg':msg})

# view for Notifications
def notification(request):
	data=models.Notifications.objects.all().order_by('-id')
	return render(request,'notification.html',{'data':data})

# view for get All Notifications
def get_notification(request):
	data=models.Notifications.objects.all().order_by('-id')
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
				'notification_detail':d.notification_detail,
				'notifStatus':notifStatus
			})
	# view for  jsonData=serializers.serialize('json', data)
	return JsonResponse({'data':jsonData,'totalUnread':totalUnread})

# view for  Mark Read By user
def mark_read_notif(request):
	notif=request.GET['notif']
	notif=models.Notifications.objects.get(pk=notif)
	user=request.user
	models.NotifUserStatus.objects.create(notif=notif,user=user,status=True)
	return JsonResponse({'bool':True})

# view for  Trainer Subscribers
def trainer_subscribers(request):
	trainer=models.Trainer.objects.get(pk=request.session['trainerid'])
	trainer_subs=models.AssignSubscriber.objects.filter(trainer=trainer).order_by('-id')
	return render(request,'trainer/trainer_subscribers.html',{'trainer_subs':trainer_subs})

# view for  Trainer Payments
def trainer_payments(request):
	trainer=models.Trainer.objects.get(pk=request.session['trainerid'])
	trainer_pays=models.TrainerSalary.objects.filter(trainer=trainer).order_by('-id')
	return render(request, 'trainer/trainer_payments.html',{'trainer_pays':trainer_pays})


# view for  Trainer Notification
def trainer_notifications(request):
	data=models.TrainerNotification.objects.all().order_by('-id')
	return render(request,'trainer/notification.html',{'notifs':data})


# view for  password change trainer
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


# view for  Trainer Messages
def trainer_msgs(request):
	data=models.TrainerMsg.objects.all().order_by('-id')
	return render(request, 'trainer/messages.html',{'msgs':data})

# view for  update user
def updateToUser(request):
	trainer=models.Trainer.objects.get(id=request.session['trainerid'])
	message=''
	if request.method=='POST':
		form=forms.updateUserForm(request.POST)
		if form.is_valid():
			updateForm=form.save(commit=False)
			updateForm.updateFromTrainer=trainer
			updateForm.save()
			message='update has been sent'
		else:
			message='Invalid update'
	form=forms.updateUserForm	
	return render(request,'updateToUser.html',{'form':form,'message':message})

# view for  update trainer
def updateToTrainer(request):
	member=request.user
	message=''
	if request.method=='POST':
		form=forms.updateTrainerForm(request.POST)
		if form.is_valid():
			updateForm=form.save(commit=False)
			updateForm.updateFromUser=member
			updateForm.save()
			message='update has been sent'
		else:
			message='Invalid update'
	form=forms.updateTrainerForm	
	return render(request,'updateToTrainer.html',{'form':form,'message':message})

def reach_us(request):
	return render(request,'reach_us.html')