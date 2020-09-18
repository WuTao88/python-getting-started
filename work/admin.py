from django.contrib import admin
from work import models
from work.models import accounts,notes,talkings
# Register your models here.

admin.site.site_header="MK"
admin.site.site_title="MK"

admin.site.register([accounts,notes,talkings])