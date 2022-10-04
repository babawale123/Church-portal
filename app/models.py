from django.db import models
from embed_video.fields import EmbedVideoField



class pastor_desk(models.Model):
	subject = models.CharField(max_length=200)
	slug = models.SlugField()
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.subject
	def snippet(self):
	  	return self.message[:100] + '....'

class Videos(models.Model):
	 video = EmbedVideoField() # same like models.URLField()
	 topic = models.CharField(max_length=100)
	 date = models.DateTimeField(auto_now_add=True)

class Audios(models.Model):
	 video = EmbedVideoField() # same like models.URLField()
	 topic = models.CharField(max_length=100)
	 date = models.DateTimeField(auto_now_add=True)

	 

class Audio(models.Model):
	audio = EmbedVideoField() # same like models.URLField()
	topic = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)


class Contact_Form(models.Model):
	name = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.name

class Gallary(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name


#Church Units

class Pastorate(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Pastors(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Choir(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Ushers(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Media(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Decoration(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Sanitation(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Security(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Protocol(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Sunday(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Technical(models.Model):
	name = models.CharField(max_length=200)
	fbook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name

class Events(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	# slug = models.SlugField()
	# fbook = models.CharField(max_length=200)
	# twitter = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name
	def snippet(self):
	  	return self.description[:100] + '....'

class Event(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.jpg', blank=True)
	
	def __str__(self):
		return self.name
	def snippet(self):
	  	return self.description[:100] + '....'


class Banner(models.Model):
	description = models.TextField()
	thumb = models.ImageField(default='default.jpg', blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.description
	


class slider(models.Model):
	first = models.TextField()
	second = models.TextField()
	thumb = models.ImageField(default='default.jpg', blank=True)
	date = models.DateTimeField(auto_now_add=True)

	
	def __str__(self):
		return self.first


		
