from django.contrib import admin
from .models import User,Badges,Hub,UserProfile,Batch

admin.site.register(User)
admin.site.register(Hub)
admin.site.register(UserProfile)
admin.site.register(Badges)
admin.site.register(Batch)
