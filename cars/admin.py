from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Cars, Category, Hesh, NetWorkLink

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model','data', 'is_publish', 'get_image')
    list_display_links = ('name', )
    list_editable = ('is_publish',)
    list_filter = ('category', 'teg', 'is_publish', 'data')
    search_fields = ('category', 'name')
    readonly_fields = ('views', 'data', 'updata', 'get_full_image')


    @admin.display(description='Изображение')
    def get_full_image(self, cars):
        return mark_safe(f'<img src={cars.photo.url} width="50%" />')


    @admin.display(description='Изображение')
    def get_image(self, cars):
        return mark_safe(f'<img src={cars.photo.url} width="50px" />')

admin.site.register(Category)
admin.site.register(Hesh)
admin.site.register(NetWorkLink)
