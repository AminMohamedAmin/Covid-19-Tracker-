from django.contrib import admin
from .models import news, advices, questions, Contacts

# Register your models here.



class NewsModelAdmin(admin.ModelAdmin):
	list_display = ["content","puplish"]
	class Meta:
		model = news

admin.site.register(news,NewsModelAdmin)


class AdviceModelAdmin(admin.ModelAdmin):
	list_display = ["content","puplish"]
	class Meta:
		model = advices

admin.site.register(advices,AdviceModelAdmin)


class QuestionModelAdmin(admin.ModelAdmin):
	list_display = ["content","puplish"]
	class Meta:
		model = questions

admin.site.register(questions,QuestionModelAdmin)

class ContactModelAdmin(admin.ModelAdmin):
	list_display = ["content","puplish"]
	class Meta:
		model = Contacts

admin.site.register(Contacts,ContactModelAdmin)