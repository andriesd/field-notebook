from django.contrib import admin


from .models import Object, Creator, Place

admin.site.register(Object)
admin.site.register(Creator)
admin.site.register(Place)
