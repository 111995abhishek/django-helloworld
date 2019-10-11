from django.contrib import admin

from.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display=('book_name','price','available','Isbn')
    list_filter=('available',)

admin.site.register(Book, BookAdmin)



