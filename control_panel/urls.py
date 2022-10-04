from django.urls import path

from newsletter.views import control_newsletter, control_newsletter_list


app_name = 'control'
urlpatterns = [
	path('newsletter/', control_newsletter, name='control_newsletter'),
	path('newsletter-list/', control_newsletter_list, name='control_newsletter_list'),
]