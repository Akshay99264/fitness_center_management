from django.shortcuts import render
from . import models
from . import forms
# Create your views here.
def home(request):
    banners=models.Banners.objects.all()
    #fetch only starting 3 services
    services=models.Service.objects.all()[:3]
    return render(request, 'home.html',{'banners':banners,'services':services})

#PageDetail
def page_detail(request,id):
	page=models.Page.objects.get(id=id)
	return render(request, 'page.html',{'page':page})

#FAQ
def faq_list(request):
	faq=models.Faq.objects.all()
	return render(request, 'faq.html',{'faq':faq})

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
