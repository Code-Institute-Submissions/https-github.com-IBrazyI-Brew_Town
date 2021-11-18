from django.contrib import admin
from .models import Review, Comments

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Review, ReviewAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'body', 'created_on')
    list_filter = ('created_on')
    search_fields = ('review', 'user', 'body')
    
admin.site.register(Comments, CommentAdmin)