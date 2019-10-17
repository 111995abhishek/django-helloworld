from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    stock=models.IntegerField(default=1)
    price=models.IntegerField()
    available=models.BooleanField()
    Isbn=models.IntegerField()

    def __str__(self):
        return self.book_name +" "+ str(self.price)

    def get_b_name(self):
        return self.book_name

class Author(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Member(models.Model):
    member_id=models.IntegerField()
    member_name=models.CharField(max_length=200)
    phone_number=models.IntegerField()
    email_id=models.EmailField(max_length=200)

    def __str__(self):
        return str(self.member_id)+""+str(self.member_name)+""+str(self.phone_number)+""+str(self.email_id)

class Record(models.Model):
    member_id=models.ForeignKey(Member,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    issue_date=models.DateField()
    return_date=models.DateField()
    is_returned=models.BooleanField(default=False)

    def __str__(self):
        return str(self.issue_date) +" "+str(self.return_date)





@receiver(post_save, sender=Record)
def update_stock(sender, instance, **kwargs):
    book = instance.book
    if instance.is_returned:
        book.stock = book.stock + 1
        book.save()
    else:
        if book.stock > 0:
            book.stock = book.stock - 1
            book.save()








