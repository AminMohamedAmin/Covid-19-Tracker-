from django.contrib import admin
from .models import Assure
# Register your models here.


class AssurModelAdmin(admin.ModelAdmin):
	list_display = ["name","age","gender","address"]
	class Meta:
		model = Assure

admin.site.register(Assure,AssurModelAdmin)