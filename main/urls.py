from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    path('pagedetail/<int:id>',views.page_detail,name='pagedetail'),
    path('faq',views.faq_list,name='faq'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('gallery',views.gallery,name='gallery'),
    path('gallerydetail/<int:id>',views.gallery_detail,name='gallery_detail'),
    path('pricing',views.pricing,name='pricing'),
    path('accounts/signup',views.signup,name='signup'),
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
    path('trainer_changePassword',views.trainer_changePassword,name='trainer_changePassword'),
    path('trainer_notifs',views.trainer_notifs,name='trainer_notifs'),
    #Notifications
    path('notification',views.notification,name='notification'),
    path('get_notification',views.get_notification,name='get_notification'),
    path('mark_read_notif',views.mark_read_notif,name='mark_read_notif'),
    # Messages
	path('messages',views.trainer_msgs,name='messages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

