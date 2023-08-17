from django.contrib import admin
from .models import Post,VideoPost,ImagePost,ArticlePost,PostComment

admin.site.register(Post)
admin.site.register(VideoPost)
admin.site.register(ImagePost)
admin.site.register(ArticlePost)
admin.site.register(PostComment)
