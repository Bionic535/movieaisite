from django.contrib import admin
from .models import UserFilmList
# Register your models here.
@admin.register(UserFilmList)
class UserFilmListAdmin(admin.ModelAdmin):
    list_display = ['username', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['username']