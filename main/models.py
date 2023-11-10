from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# slideShow
class SlideShow(models.Model):
	img=models.ImageField(upload_to="slideShow/")
	alt_text=models.CharField(max_length=150)

	class Meta:
		verbose_name_plural='SlideShow'

	def __str__(self):
		return self.alt_text

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url))

# Create your models here.
class ourOfferings(models.Model):
	title=models.CharField(max_length=150)
	detail=models.TextField()
	img=models.ImageField(upload_to="ourOfferings/",null=True)
	
	class Meta:
		verbose_name_plural='ourOfferings'

	def __str__(self):
		return self.alt_text

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url))



#pages models
class Page(models.Model):
	label=models.CharField(max_length=200)
	description=models.TextField()

	def __str__(self):
		return self.label

#FAQ
class Faq(models.Model):
	question=models.TextField()
	answer=models.TextField()

	def __str__(self):
		return self.question

#query Model
class Queries(models.Model):
	Name=models.CharField(max_length=150)
	email=models.CharField(max_length=150)
	description=models.TextField()
	time=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural='Queries'
	
	def __str__(self):
		return self.Name

#gallery model
class FunEvents(models.Model):
	label=models.CharField(max_length=150)
	description=models.TextField()
	image=models.ImageField(upload_to="funEvents/",null=True)

	class Meta:
		verbose_name_plural='FunEvents'

	def __str__(self):
		return self.label

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.image.url))

#gallery image
class EventImages(models.Model):
	event=models.ForeignKey(FunEvents,on_delete=models.CASCADE,null=True)
	detail=models.CharField(max_length=150)
	image=models.ImageField(upload_to="event_images/",null=True)

	class Meta:
		verbose_name_plural='EventImages'

	def __str__(self):
		return self.detail

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.image.url))


# Subscription plan
class SubPlan(models.Model):
	title=models.CharField(max_length=150)
	price=models.IntegerField()
	max_member=models.IntegerField(null=True)
	highlight_status=models.BooleanField(default=False,null=True)
	validity_days=models.IntegerField(null=True)

	def __str__(self):
		return self.title


# Subscription plan features
class SubPlanFeature(models.Model):
	subplan=models.ForeignKey(SubPlan, on_delete=models.CASCADE, default=None, null=True)
	title=models.CharField(max_length=150)

	def __str__(self):
		return self.title



# Subscriber
class Subscriber(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
	mobile=models.CharField(max_length=20)
	address=models.TextField()
	img=models.ImageField(upload_to="subs/")

	def __str__(self):
		return str(self.user)

	def image_tag(self):
		if self.img:
			return mark_safe('<img src="%s" width="80" />' % (self.img.url))
		else:
			return 'no-image'
		
@receiver(post_save,sender=User)
def create_subscriber(sender,instance,created,**kwrags):
	if created:
		Subscriber.objects.create(user=instance)

# Subscription
class Members(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	plan=models.ForeignKey(SubPlan, on_delete=models.CASCADE,null=True)
	price=models.CharField(max_length=50)
	register_date=models.DateField(auto_now_add=True,null=True)

	class Meta:
		verbose_name_plural='Members'

#Trainer
class Trainer(models.Model):
	full_name=models.CharField(max_length=100)
	username=models.CharField(max_length=100,null=True)
	password=models.CharField(max_length=50,null=True)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	is_active=models.BooleanField(default=False)
	detail=models.TextField()
	img=models.ImageField(upload_to="trainers/")
	salary=models.IntegerField(default=0)
	facebook=models.CharField(max_length=200,null=True)
	twitter=models.CharField(max_length=200,null=True)
	pinterest=models.CharField(max_length=200,null=True)
	youtube=models.CharField(max_length=200,null=True)


	def __str__(self):
		return str(self.full_name)

	def image_tag(self):
		if self.img:
			return mark_safe('<img src="%s" width="80" />' % (self.img.url))
		else:
			return 'no-image'

# Notifications Json Response Via Ajax
class Notifications(models.Model):
	notification_detail=models.TextField()
	userRead=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	trainerRead=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,blank=True)

	class Meta:
		verbose_name_plural='Notification'

	def __str__(self):
		return str(self.notification_detail)

# Model to mark as read notification by user
class NotifUserStatus(models.Model):
	notif=models.ForeignKey(Notifications, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	status=models.BooleanField(default=False)

	class Meta:
		verbose_name_plural='Notification Status'

# Assign Subscriber to trainer
class AssignSubscriber(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)

# Trainer Achivements
class TrainerAchivement(models.Model):
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	detail=models.TextField()
	img=models.ImageField(upload_to="trainers_achivements/")

	def __str__(self):
		return str(self.title)

	def image_tag(self):
		if self.img:
			return mark_safe('<img src="%s" width="80" />' % (self.img.url))
		else:
			return 'no-image'

# TrainerSalary Model
class TrainerSalary(models.Model):
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
	amt=models.IntegerField()
	amt_date=models.DateField()
	remarks=models.TextField(blank=True)

	class Meta:
		verbose_name_plural='Trainer Salary'

	def __str__(self):
		return str(self.trainer.full_name)

# Trainer Notifications
class TrainerNotification(models.Model):
	notif_msg=models.TextField()

	class Meta:
		verbose_name_plural='TrainerNotification'


	def __str__(self):
		return str(self.notif_msg)

# Markas Read Notification By Trainer
class NotifTrainerStatus(models.Model):
	notif=models.ForeignKey(TrainerNotification, on_delete=models.CASCADE)
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
	status=models.BooleanField(default=False)

	class Meta:
		verbose_name_plural='TrainerNotificationStatus'


# SubscriberMsg
class TrainerMsg(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True)
	message=models.TextField()

	class Meta:
		verbose_name_plural='TrainerMessages'

# SubscriberMsg
class UserMsg(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True)
	message=models.TextField()

	class Meta:
		verbose_name_plural='UserMessages'


# send update
class userTrainerUpdate(models.Model):
	updateToTrainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,related_name='updateToTrainer')
	updateToUser=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='updateToUser')
	updateFromTrainer=models.ForeignKey(Trainer, on_delete=models.CASCADE,null=True,related_name='updateFromTrainer',blank=True)
	updateFromUser=models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='updateFromUser',blank=True)
	updateMsg=models.TextField()
