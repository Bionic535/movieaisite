from django.contrib import admin
from .models import UserFilmList
# Register your models here.
@admin.register(UserFilmList)
class UserFilmListAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'created_at', 'updated_at']  # <-- changed 'user' to 'user_id'
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user_id']  # <-- changed 'user__username' to 'user_id'