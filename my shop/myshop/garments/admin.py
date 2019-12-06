from django.contrib import admin
from garments.models import FormalShirt
from garments.models import CasualShirt
from garments.models import FormalTrousers
class FormalShirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

class CasualShirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

class FormalTrousersAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

# Register your models here.
admin.site.register(FormalShirt, FormalShirtAdmin)
admin.site.register(CasualShirt, CasualShirtAdmin)
admin.site.register(FormalTrousers, FormalTrousersAdmin)