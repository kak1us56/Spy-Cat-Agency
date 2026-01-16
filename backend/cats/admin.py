from django.contrib import admin

from .models import Cat, Mission, Target

@admin.register(Cat)
class SMSMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "years_of_experience", "salary", "breed"]