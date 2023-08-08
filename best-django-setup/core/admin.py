from django.contrib import admin
from .forms import CustomUsercreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUsercreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)