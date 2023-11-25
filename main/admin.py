from django.contrib import admin
from . import models
#Registerd the model SlideShow on admin panel
class SlideShowAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')
admin.site.register(models.SlideShow,SlideShowAdmin)

#Registerd the model OurOfferings on admin panel
class ourOfferingsAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.ourOfferings,ourOfferingsAdmin)
 
#Registerd the model Page on admin panel
class PageAdmin(admin.ModelAdmin):
	list_display=('label',)
admin.site.register(models.Page,PageAdmin)

#Registerd the model Faq on admin panel
class FaqAdmin(admin.ModelAdmin):
	list_display=('question',)
admin.site.register(models.Faq,FaqAdmin)

#Registerd the model Queries on admin panel
class QueriesAdmin(admin.ModelAdmin):
	list_display=('Name','email','description','time')
admin.site.register(models.Queries,QueriesAdmin)

#Registerd the model FunEvents on admin panel
class FunEventsAdmin(admin.ModelAdmin):
	list_display=('label','image_tag')
admin.site.register(models.FunEvents,FunEventsAdmin)

#Registerd the model EventImages on admin panel
class EventImagesAdmin(admin.ModelAdmin):
	list_display=('detail','image_tag')
admin.site.register(models.EventImages,EventImagesAdmin)

#Registerd the model SubPlan on admin panel
class SubPlanAdmin(admin.ModelAdmin):
	list_editable=('highlight_status','max_member')
	list_display=('title','price','max_member','validity_days','highlight_status')
admin.site.register(models.SubPlan,SubPlanAdmin)

#Registerd the model SubPlanFeatures on admin panel
class SubPlanFeatureAdmin(admin.ModelAdmin):
	list_display=('title','subplan')
admin.site.register(models.SubPlanFeature,SubPlanFeatureAdmin)

#Registerd the model Subscriber on admin panel
class SubscriberAdmin(admin.ModelAdmin):
	list_display=('user','image_tag','mobile')
admin.site.register(models.Subscriber,SubscriberAdmin)

#Registerd the model Members on admin panel
class MembersAdmin(admin.ModelAdmin):
	list_display=('user','plan','register_date','price')
admin.site.register(models.Members,MembersAdmin)

#Registerd the model Trainer on admin panel
class TrainerAdmin(admin.ModelAdmin):
	list_editable=('is_active',)
	list_display=('full_name','mobile','salary','is_active','image_tag')
admin.site.register(models.Trainer,TrainerAdmin)

#Registerd the model SlideShow on admin panel
class NotificationsAdmin(admin.ModelAdmin):
	list_display=('notification_detail','userRead','trainerRead')
admin.site.register(models.Notifications,NotificationsAdmin)

#Registerd the model NotifUserStatus on admin panel
class NotifUserStatusAdmin(admin.ModelAdmin):
	list_display=('notif','user','status')
admin.site.register(models.NotifUserStatus,NotifUserStatusAdmin)

#Registerd the model AssinSubscriber on admin panel
class AssignSubscriberAdmin(admin.ModelAdmin):
	list_display=('trainer','user')
admin.site.register(models.AssignSubscriber,AssignSubscriberAdmin)

#Registerd the model TrainerAchivement on admin panel
class TrainerAchivementAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(models.TrainerAchivement,TrainerAchivementAdmin)

#Registerd the model TrainerSalary on admin panel
class TrainerSalaryAdmin(admin.ModelAdmin):
	list_display=('trainer','amt','amt_date')
admin.site.register(models.TrainerSalary,TrainerSalaryAdmin)

#Registerd the model TrainerNotification on admin panel
class TrainerNotificationAdmin(admin.ModelAdmin):
	list_display=('notif_msg',)
admin.site.register(models.TrainerNotification,TrainerNotificationAdmin)

#Registerd the model TrainerMsg on admin panel
class TrainerMsgAdmin(admin.ModelAdmin):
	list_display=('user','trainer','message')
admin.site.register(models.TrainerMsg,TrainerMsgAdmin)

#Registerd the model UserMsg on admin panel
class UserMsgAdmin(admin.ModelAdmin):
	list_display=('trainer','user','message')
admin.site.register(models.UserMsg,UserMsgAdmin)

#Registerd the model userTrainerUpdate on admin panel
class userTrainerUpdateAdmin(admin.ModelAdmin):
	list_display=('updateMsg','updateToTrainer','updateToUser','updateFromTrainer','updateFromUser')
admin.site.register(models.userTrainerUpdate,userTrainerUpdateAdmin)

