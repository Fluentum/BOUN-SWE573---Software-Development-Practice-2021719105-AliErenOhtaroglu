from django.contrib import admin

from .models import Post

#, Category

admin.site.register(Post)

#admin.site.register(Category)

# registered the post model for the admin page.
# models can be called from different pages.