from django.contrib import admin
from users.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'us_imageine', 'us_birthday', 'us_ciudad', 'us_isactive', 'username', 'password', 'email', 'updated_at')

# Register your models here.
admin.site.register(User, UserAdmin)




