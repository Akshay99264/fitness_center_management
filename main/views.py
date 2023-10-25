from django.shortcuts import render,redirect
from . import models
from . import forms
# Create your views here.
def home(request):
	banners=models.Banners.objects.all()
	services=models.Service.objects.all()[:3]
	gimgs=models.GalleryImage.objects.all().order_by('-id')[:9]
	return render(request, 'home.html',{'banners':banners,'services':services,'gimgs':gimgs})

#PageDetail
def page_detail(request,id):
	page=models.Page.objects.get(id=id)
	return render(request, 'page.html',{'page':page})

#FAQ
def faq_list(request):
	faq=models.Faq.objects.all()
	return render(request, 'faq.html',{'faqs':faq})

#Enquiry
def enquiry(request):
    msg=''
    if request.method=='POST':
        form=forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg='Data has been saved'
    form=forms.EnquiryForm
    return render(request, 'enquiry.html',{'form':form,'msg':msg})


# show galleries
def gallery(request):
	gallery=models.Gallery.objects.all().order_by('-id')
	return render(request, 'gallery.html',{'gallerys':gallery})

# Show gallery photos
def gallery_detail(request,id):
	gallery=models.Gallery.objects.get(id=id)
	gallery_imgs=models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
	return render(request, 'gallery_imgs.html',{'gallery_imgs':gallery_imgs,'gallery':gallery})

#Subscription Plans
def pricing(request):
	pricing=models.SubPlan.objects.all()
	dfeatures=models.SubPlanFeature.objects.distinct('title')
	return render(request, 'pricing.html',{'plans':pricing,'dfeatures':dfeatures})

def signup(request):
	msg=None
	if request.method=='POST':
		form=forms.SignUp(request.POST)
		if form.is_valid():
			form.save()
			msg='Thank you for register.'
	form=forms.SignUp
	return render(request, 'registration/signup.html',{'form':form,'msg':msg})


# User Dashboard implementation starts here
def user_dashboard(request):
	return render(request,'user/dashboard.html')

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
	return render(request, 'trainer/login.html',{'form':form,'msg':msg})

# TrainerLogout
def trainerlogout(request):
	del request.session['trainerLogin']
	return redirect('/trainerlogin')