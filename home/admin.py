from django.contrib import admin
from .models import Contact, UserProfileInfo, YoutubeVideos

# Register your models here.
admin.site.register(Contact)
admin.site.register(UserProfileInfo)
admin.site.register(YoutubeVideos)
