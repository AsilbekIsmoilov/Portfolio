from django.contrib import admin

from portfolio.models import Category, Info, Gallery, About, Experience, Projects


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['id','title']

class GalleryAdmin(admin.TabularInline):
    model = Gallery
    fk_name = 'info'
    extra = 1

class InfoAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    prepopulated_fields = {'slug':('title',)}
    inlines =[GalleryAdmin]


admin.site.register(Category,CategoryAdmin)
admin.site.register(Info,InfoAdmin)
admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Projects)