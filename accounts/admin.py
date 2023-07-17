from django.contrib import admin
from .models import User,Badges,Hub,UserProfile,Batch,LoginWithEmailData,Stack

admin.site.register(User)
admin.site.register(Hub)
admin.site.register(UserProfile)
admin.site.register(Badges)
admin.site.register(Batch)
admin.site.register(LoginWithEmailData)
admin.site.register(Stack)
