from django.contrib import admin
from ciudades.models import Estado, Ciudad
# Register your models here.

class EstadoAdmin(admin.ModelAdmin):
	list_display = ('estado_name', 'updated_at')

class CiudadAdmin(admin.ModelAdmin):
	list_display = ('ciudad_name', 'ciudad_estado', 'updated_at')

# Register your models here.
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Ciudad, CiudadAdmin)




