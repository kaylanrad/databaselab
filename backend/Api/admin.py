from django.contrib import admin
from Api.models import Book, Author, Publisher, Genre, Translator


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name','pen_name','is_alive')



class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)



class PublisherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address','phone_number')



class TranslatorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'translate_lang')

admin.site.register(Book)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Translator,TranslatorAdmin)