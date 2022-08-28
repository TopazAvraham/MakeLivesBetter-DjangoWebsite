from django.contrib import admin
from .models import Feature
from .models import UserExtend
from .models import Stores
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserExtendInLine(admin.StackedInline):
    model = UserExtend
    can_delete = False
    verbose_name_plural = 'UserExtend'


class CustomizeUserAdmin(UserAdmin):
    inlines= (UserExtendInLine, )



admin.site.unregister(User)
admin.site.register(User, CustomizeUserAdmin)
admin.site.register(Feature)
admin.site.register(UserExtend)
admin.site.register(Stores)
admin.site.register(Post)


