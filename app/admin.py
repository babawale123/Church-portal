from django.contrib import admin
from . models import  pastor_desk,Videos, Audio,Contact_Form,Gallary,Pastors,Choir,Ushers,Media,Decoration,Sanitation,Security,Protocol,Audios,slider,Sunday,Technical,Events,Event,Banner
from embed_video.admin import AdminVideoMixin 


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin): 
	pass
admin.site.register(Videos, MyModelAdmin)
admin.site.register(Audios, MyModelAdmin)

admin.site.register(pastor_desk)
admin.site.register(Contact_Form)
admin.site.register(Gallary)

admin.site.register(Pastors)
admin.site.register(Choir)
admin.site.register(Ushers)
admin.site.register(Media)
admin.site.register(Decoration)
admin.site.register(Sanitation)
admin.site.register(Security)
admin.site.register(Protocol)
admin.site.register(Sunday)
admin.site.register(Technical)
admin.site.register(Event)
# admin.site.register(Banner)

# admin.site.register(slider)



