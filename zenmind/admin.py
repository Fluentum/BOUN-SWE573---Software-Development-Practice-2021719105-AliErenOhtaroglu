from django.contrib import admin

from .models import Post # imported post model

admin.site.register(Post) #registered the post model for the adming page.
#models can be called from different pages.
