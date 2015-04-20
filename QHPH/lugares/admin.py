from django.contrib import admin

from .models import Lugar

class LugarAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'ciudad']

admin.site.register(Lugar, LugarAdmin)