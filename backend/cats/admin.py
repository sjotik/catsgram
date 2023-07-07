from django.contrib import admin

from .models import Achievement, Cat


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'birth_year', 'owner')
    search_fields = ('name',)
    list_filter = ('color', 'birth_year',)
    empty_value_display = '-пусто-'


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Cat, CatAdmin)
