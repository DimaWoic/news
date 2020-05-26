from django.contrib import admin

# Register your models here.
from .models import News, Category, Messages, City, CityNews, Weather


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('published', 'category', 'title', 'description')
    list_display_links = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    model = Category


class MassagesAdmin(admin.ModelAdmin):
    model = Messages
    list_display = ('published', 'name', 'email', 'text')


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ('name', 'source',)

class CityNewsAdmin(admin.ModelAdmin):
    model = CityNews
    list_display = ('published', 'title', 'description', 'city')

class WetherAdmin(admin.ModelAdmin):
    model = Weather
    list_display = '__all__'


admin.site.register(CityNews, CityNewsAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Messages, MassagesAdmin)