from django.contrib import admin
from .models import Feature, Approval, ApprovedPost
from .models import UserExtend
from .models import Store
from .models import VolunteeringOption
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Category


# Register your models here.
class UserExtendInLine(admin.StackedInline):
    model = UserExtend
    can_delete = False
    verbose_name_plural = 'UserExtend'


class CustomizeUserAdmin(UserAdmin):
    inlines = (UserExtendInLine,)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.unregister(User)
admin.site.register(User, CustomizeUserAdmin)
admin.site.register(Feature)
admin.site.register(UserExtend)
admin.site.register(Store)
admin.site.register(VolunteeringOption, PostAdmin)
admin.site.register(Category)
admin.site.register(Approval)
admin.site.register(ApprovedPost)
