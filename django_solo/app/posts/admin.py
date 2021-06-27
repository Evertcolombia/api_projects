from django.contrib import admin

# models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Post admin """
    list_display = ('pk', 'title', 'user', 'created_at')
    list_display_links = ('pk',)
    list_editable = ('title',)

    search_fields = (
        'user__username',
        'title'
    )



