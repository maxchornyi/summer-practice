from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags","date")
    list_display = ("title", "date","author",)
    prepopulated_fields = {"slug": ("title",)}

#class BookAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("title",)}
#    list_filter = ("author", "rating",)
#    list_display = ("title", "author",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
