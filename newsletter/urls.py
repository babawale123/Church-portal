from django.urls import path
from . import views

app_name = 'newsletter'

urlpatterns = [
	path('sign_up/', views.newsletter_signup, name="sign_up"),
	path('unsubscribe',views.newsletter_unsubscribe, name="unsubscribe"),
]