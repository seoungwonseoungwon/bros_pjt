from django.contrib import admin
from .models import TeamList, Hitting, Pitcher
# Register your models here.

admin.site.register(TeamList)
admin.site.register(Hitting)
admin.site.register(Pitcher)
