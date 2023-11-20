from django.contrib import admin

from social.models import Subscription, Comment, BlogPost, UserProfile, Like

admin.site.register(UserProfile)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Subscription)