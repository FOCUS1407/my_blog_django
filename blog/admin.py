from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published', 'created_at')
    list_filter = ('published', 'category')
    search_fields = ['title', 'desc']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
