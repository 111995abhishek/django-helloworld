from django.contrib import admin

from.models import Book,Author,Member,Record


class BookAdmin(admin.ModelAdmin):
    list_display=('book_name','price','available','stock','Isbn')
    list_filter=('available',)

admin.site.register(Book,BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Author,AuthorAdmin)


class MemberAdmin(admin.ModelAdmin):
    list_display=('member_id','member_name','phone_number','email_id')

admin.site.register(Member,MemberAdmin)


class RecordAdmin(admin.ModelAdmin):
    list_display=('member_id','book','issue_date','return_date')

admin.site.register(Record,RecordAdmin)



