from django.contrib import admin

from flag.models import FlaggedContent, FlagInstance, FlagCategory


class FlagCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(FlagCategory, FlagCategoryAdmin)

class InlineFlagInstance(admin.TabularInline):
    model = FlagInstance
    extra = 0


class FlaggedContentAdmin(admin.ModelAdmin):
    inlines = [InlineFlagInstance]


admin.site.register(FlaggedContent, FlaggedContentAdmin)
