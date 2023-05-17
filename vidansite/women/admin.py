from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)  # Позволяет вкл/выкл публикацию в админке
    list_filter = ('is_published', 'time_create')  # Включает категории по которым возможна фильтрации в админке
    prepopulated_fields = {'slug': ('title',)}
    fields = ('get_html_photo', 'title', 'slug', 'cat', 'content', 'photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=60>")

    get_html_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # Обязательно ставить запятую - обозначая что передаем кортеж(если элемент всего 1)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = "Админ-панель сайта о известных женщинах"
admin.site.site_header = "Админ-панель сайта о известных женщинах"
