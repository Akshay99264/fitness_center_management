from django.contrib import admin
from . import models

class SlideShowAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag')
admin.site.register(models.SlideShow,SlideShowAdmin)

class ourOfferingsAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.ourOfferings,ourOfferingsAdmin)
 
class PageAdmin(admin.ModelAdmin):
	list_display=('label',)
admin.site.register(models.Page,PageAdmin)

class FaqAdmin(admin.ModelAdmin):
	list_display=('question',)
admin.site.register(models.Faq,FaqAdmin)

class QueriesAdmin(admin.ModelAdmin):
	list_display=('Name','email','description','time')
admin.site.register(models.Queries,QueriesAdmin)

class FunEventsAdmin(admin.ModelAdmin):
	list_display=('label','image_tag')
admin.site.register(models.FunEvents,FunEventsAdmin)

class EventImagesAdmin(admin.ModelAdmin):
	list_display=('detail','image_tag')
admin.site.register(models.EventImages,EventImagesAdmin)

class SubPlanAdmin(admin.ModelAdmin):
	list_editable=('highlight_status','max_member')
	list_display=('title','price','max_member','validity_days','highlight_status')
admin.site.register(models.SubPlan,SubPlanAdmin)

class SubPlanFeatureAdmin(admin.ModelAdmin):
	list_display=('title','subplan')
admin.site.register(models.SubPlanFeature,SubPlanFeatureAdmin)

class SubscriberAdmin(admin.ModelAdmin):
	list_display=('user','image_tag','mobile')
admin.site.register(models.Subscriber,SubscriberAdmin)

class MembersAdmin(admin.ModelAdmin):
	list_display=('user','plan','register_date','price')
admin.site.register(models.Members,MembersAdmin)


class TrainerAdmin(admin.ModelAdmin):
	list_editable=('is_active',)
	list_display=('full_name','mobile','salary','is_active','image_tag')
admin.site.register(models.Trainer,TrainerAdmin)


class NotificationsAdmin(admin.ModelAdmin):
	list_display=('notification_detail','userRead','trainerRead')
admin.site.register(models.Notifications,NotificationsAdmin)

class NotifUserStatusAdmin(admin.ModelAdmin):
	list_display=('notif','user','status')
admin.site.register(models.NotifUserStatus,NotifUserStatusAdmin)

class AssignSubscriberAdmin(admin.ModelAdmin):
	list_display=('trainer','user')
admin.site.register(models.AssignSubscriber,AssignSubscriberAdmin)

class TrainerAchivementAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(models.TrainerAchivement,TrainerAchivementAdmin)

class TrainerSalaryAdmin(admin.ModelAdmin):
	list_display=('trainer','amt','amt_date')
admin.site.register(models.TrainerSalary,TrainerSalaryAdmin)

class TrainerNotificationAdmin(admin.ModelAdmin):
	list_display=('notif_msg',)
admin.site.register(models.TrainerNotification,TrainerNotificationAdmin)

class TrainerMsgAdmin(admin.ModelAdmin):
	list_display=('user','trainer','message')
admin.site.register(models.TrainerMsg,TrainerMsgAdmin)

class UserMsgAdmin(admin.ModelAdmin):
	list_display=('trainer','user','message')
admin.site.register(models.UserMsg,UserMsgAdmin)


class userTrainerUpdateAdmin(admin.ModelAdmin):
	list_display=('updateMsg','updateToTrainer','updateToUser','updateFromTrainer','updateFromUser')
admin.site.register(models.userTrainerUpdate,userTrainerUpdateAdmin)

