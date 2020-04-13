from django.contrib import admin

# Register your models here.
from home.models import questionPaperDetails,subjects
from django.contrib import admin
# from django_google_maps import widgets #as map_widgets
# from django_google_maps import fields #as map_fields

# Register your models here.
@admin.register(questionPaperDetails)
class questionPaperDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(subjects)
class subjectsAdmin(admin.ModelAdmin):
    pass