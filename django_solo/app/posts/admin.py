from django.contrib import admin

# models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Post admin """
    list_display = (
        'id',
        'user',
        'title',
        'created_at'
    )
    search_fields = (
        'user__username',
        'title',
        'user__email'
    )
    list_filter = ('created_at', 'updated_at')


