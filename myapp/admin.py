from django.contrib import admin
from .models import Address,Profile
# Register your models here.


admin.site.register(Address)
# class ProfileAdmin(admin.ModelAdmin):
#     # model = Profile
#     fields = ['phone_number','gender','profile_pic']
#
# # class AddressAdmin(admin.ModelAdmin):
# #     fields = ['city','state','pincode']
# #
# #     inlines = [ProfileInline]
#
# admin.site.register(Profile,ProfileAdmin)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','profile_pic','phone_number','permanent_address')
    # readonly_fields = ('user',)
    search_fields = ('user__first_name',)
    list_filter = ['gender','permanent_address__city']


admin.site.register(Profile, ProfileAdmin)
