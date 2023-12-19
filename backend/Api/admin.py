from django.contrib import admin
from Api.models import Book, Author, Publisher, Genre, Translator, User, GateWay


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name','pen_name','is_alive')



class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)



class PublisherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address','phone_number')



class TranslatorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'translate_lang')



class GateWayAdmin(admin.ModelAdmin):
    list_display = ('user', 'price','is_paid')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_exist','is_published', 'edition_year', 'price')

admin.site.register(Book, BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Translator,TranslatorAdmin)
admin.site.register(User)
admin.site.register(GateWay, GateWayAdmin)
