from django.contrib import admin
from .models import Users, Blogs, Comments
# Register your models here.

admin.site.register(Users)
admin.site.register(Blogs)
admin.site.register(Comments)