from django.contrib import admin

# Register your models here.

from .models import Author, Topic, Post, Comment, Troll

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    
    fields = ['first_name', 'last_name', ('date_of_birth')]

# Register the Admin classes for Book using the decorator

#   Book s InstanceInline how to put there fkn plural???
class CommentInline(admin.TabularInline):
    model = Comment


#   ', display_topic'
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    
    inlines = [CommentInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'post', 'troller', 'commdatetime', 'id')
    list_filter = ('post', 'commdatetime')
    
    fieldsets = (
        (None, {
            'fields': ('troll', 'id')
        }),
        ('Post n Troll', {
            'fields': ('post', 'content')
        }),
    )


# Register the Admin classes for BookInstance using the decorator
# @admin.register(Troll)
# class TrollAdmin(admin.ModelAdmin):
    # list_display = ('last_name', 'first_name', 'date_of_birth')
    



# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#   admin.site.register(Post)
#   admin.site.register(Author)
admin.site.register(Topic)
#   admin.site.register(Comment)
admin.site.register(Troll)







