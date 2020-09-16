from django.contrib import admin

# Register your models here.
from django.contrib import admin
from garbageCollection.models import CollectionDetails


admin.site.register(CollectionDetails)