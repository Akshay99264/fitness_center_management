from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    path('pDetail/<int:id>',views.pDetail,name='pDetail'),
    path('commonQuestions',views.commonQuestions,name='commonQuestions'),
    path('query',views.query,name='query'),
    path('showcase',views.showcase,name='showcase'),
    path('showcase_data/<int:id>',views.showcase_data,name='showcase_data'),
    path('price',views.price,name='price'),
    path('accounts/newUser',views.newUser,name='newUser'),
    # User Dashboard implementations starts here
    path('user-dashboard',views.user_dashboard,name='user_dashboard'),
    path('update-profile',views.update_profile,name='update_profile'),
    #Trainer Login
    path('trainerlogin',views.trainerlogin,name='trainerlogin'),
    path('trainerlogout',views.trainerlogout,name='trainerlogout'),
    path('trainer_dashboard',views.trainer_dashboard,name='trainer_dashboard'),
    path('trainer_profile',views.trainer_profile,name='trainer_profile'),
    path('trainer_subscribers',views.trainer_subscribers,name='trainer_subscribers'),
    path('trainer_payments',views.trainer_payments,name='trainer_payments'),
    path('passwordChange_trainer',views.passwordChange_trainer,name='passwordChange_trainer'),
    path('trainer_notifications',views.trainer_notifications,name='trainer_notifications'),
    #Notifications
    path('notification',views.notification,name='notification'),
    path('get_notification',views.get_notification,name='get_notification'),
    path('mark_read_notif',views.mark_read_notif,name='mark_read_notif'),
    # Messages
	path('messages',views.trainer_msgs,name='messages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

