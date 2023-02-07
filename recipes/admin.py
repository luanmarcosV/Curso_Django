from django.contrib import admin

from .models import Category, Recipe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_published', 'author']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title', 'created_at', 'is_published', 'author']
    list_filter = ['category', 'id', 'is_published', 'author']
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('title',)
    }
    

admin.site.register(Category, CategoryAdmin)