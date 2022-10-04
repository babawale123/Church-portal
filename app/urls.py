from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('',views.home, name='home'),
    path('message/',views.message, name='message'),
    path('gallary2/',views.gallary2, name='gallary2'),
    path('gallary/',views.gallary, name='gallary'),
    path('more/',views.pastor_more, name='more'),
    path('videos/',views.videos, name='video'),
    path('audio/',views.audios_video, name='audio'),
    path('audios/',views.audios, name='audio'),
    path('events/',views.events, name='events'),
    path('pastors_unit/',views.pastors_unit, name='pastors_unit'),
    path('contact/',views.contact_us, name='contact_us'),

    #UNITS
    path('choir/',views.choir, name='choir'),
    path('usher/',views.ushers, name='ushers'),
    path('media/',views.media, name='media'),
    path('decoration/',views.decoration, name='decoration'),
    path('sanitation/',views.sanitation, name='sanitation'),
    path('protocol/',views.protocol, name='protocol'),
    path('security_unit/',views.security, name='security'),
    path('sunday_school/',views.sunday, name='sunday_school'),
    path('technical/',views.technical, name='technical'),





    path('<slug>/',views.details, name='detail'),



]