from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Category, Location


admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'is_published',
        'created_at',
        'location',
        'pub_date',
        'category',
        'text'
    )
    list_editable = (
        'author',
        'is_published',
        'location',
        'pub_date',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('author',)
    list_display_links = ('title',)
    empty_value_display = ('Не задано')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = (
        'slug',
        'is_published'
    )
    search_fields = ('title',)
    list_filter = ('slug',)
    list_display_links = ('title',)
    empty_value_display = ('Не задано')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_editable = ()
    search_fields = ('name',)
    empty_value_display = ('Не задано')
