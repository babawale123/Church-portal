from django.shortcuts import render, get_object_or_404, redirect
from . models import Audio,Audios, Videos, pastor_desk, Gallary,Pastors,Choir,Ushers,Media,Decoration,Sanitation,Security,Protocol,slider,Sunday,Technical, Event,Banner
from django.http import HttpResponse
from . forms import ContactForm
from django.contrib import messages




# Create your views here.
def home(request):
	message = pastor_desk.objects.all().order_by('slug')[:4]
	return render(request,'pages/home.html',{'wale':message})

def pastor_more(request):
	message = pastor_desk.objects.all().order_by('slug')
	return render(request, 'pages/pastor_more.html',{'wale':message})

def details(request, slug):
	context = {}
	message = get_object_or_404(pastor_desk, slug=slug)

	context['message'] = message

	return render(request, 'pages/pastor_detail.html', context)

def videos(request):
	video = Videos.objects.all().order_by('-date')
	return render(request, 'pages/videos.html',{'wale':video})

def audios_video(request):
	video = Audios.objects.all().order_by('-date')
	return render(request, 'pages/audio.html',{'wale':video})

def audios(request):
	audio = Audio.objects.all().order_by('-audio')
	return render(request, 'pages/audio.html',{'wale':audio})



def contact_us(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('app:message')

	
	else:
		form = ContactForm()
	return render(request, 'pages/contact_form.html', {'form':form})

def message(request):
	return render(request, 'pages/messages.html')

def gallary(request):
	gallary = Gallary.objects.all().order_by('-date')
	return render(request,'pages/gallary.html',{'wale':gallary})

def gallary2(request):
	gallary = Gallary.objects.all()
	return render(request,'pages/gallary2.html',{'wale':gallary})

def pastors_unit(request):
	pastors = Pastors.objects.all()
	return render(request, 'pages/pastors_unit.html',{'wale':pastors})

#UNITS

def choir(request):
	choir = Choir.objects.all()
	return render(request, 'units/choir.html',{'wale':choir})

def ushers(request):
	choir = Ushers.objects.all()
	return render(request, 'units/ushers.html',{'wale':choir})

def media(request):
	media = Media.objects.all()
	return render(request, 'units/media.html',{'wale':media})

def decoration(request):
	decoration = Decoration.objects.all()
	return render(request, 'units/decoration.html',{'wale':decoration})

def sanitation(request):
	sanitation = Sanitation.objects.all()
	return render(request, 'units/sanitation.html',{'wale':sanitation})

def protocol(request):
	protocol = Protocol.objects.all()
	return render(request, 'units/protocol.html',{'wale':protocol})

def security(request):
	security = Security.objects.all()
	return render(request, 'units/security.html',{'wale':security})

def sunday(request):
	sunday = Sunday.objects.all()
	return render(request, 'units/sunday.html',{'wale':sunday})

def technical(request):
	technical = Technical.objects.all()
	return render(request, 'units/Technical.html',{'wale':technical})

def events(request):
	events = Event.objects.all().order_by('-date')[:3]
	return render(request, 'pages/events.html',{'events':events})

def banner(request):
	banner = Event.objects.all().order_by('-date')[:1]
	return render(request, 'pages/home.html',{'banner':banner})




