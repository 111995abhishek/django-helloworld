from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    price=models.IntegerField()
    available=models.BooleanField()
    Isbn=models.IntegerField()

    def __str__(self):
        return self.book_name+""+str(self.price)

