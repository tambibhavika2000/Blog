from django.contrib import admin

from .models import Articles,News,Interview
admin.site.register(Articles)
admin.site.register(Interview)
admin.site.register(News)