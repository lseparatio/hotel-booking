from django.contrib import admin
from .models import TopNav,IndexPage
from parler.admin import TranslatableAdmin


admin.site.register(TopNav, TranslatableAdmin)
admin.site.register(IndexPage, TranslatableAdmin)
