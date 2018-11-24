from django.contrib import admin
from example_app.models import AccessRecord, Topic, Webpage, Userinos, UserProfileInfo

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Userinos)
admin.site.register(UserProfileInfo)
