from django.contrib import admin
from .models import *
# Register your models here.\

admin.site.register(Users)
admin.site.register(Posts)
admin.site.register(Collections)
admin.site.register(Posts_collection)
admin.site.register(Users_followers)
admin.site.register(Bookmarks)
admin.site.register(Users_collections)
admin.site.register(Analytics)
admin.site.register(Comments)
admin.site.register(Users_following)