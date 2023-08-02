from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_data",)

# Register your models here.
admin.site.register(Member, MemberAdmin)
