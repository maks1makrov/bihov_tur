from django.contrib import admin

from tourism.models import Enterpreneurs, Toursites, Articles, Field_of_activity

admin.site.register(Field_of_activity)
admin.site.register(Enterpreneurs)
admin.site.register(Toursites)
admin.site.register(Articles)