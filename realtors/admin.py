from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id','name','email','phone', 'hire_date','is_mvp')
	list_display_links = ('name',)
	list_editable = ('is_mvp',)
	search_field =('name',)
	list_per_page = 25
	


admin.site.register(Realtor,RealtorAdmin)
