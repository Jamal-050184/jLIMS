from django.db import models

# Create your models here.

class Library(models.Model):
   id = models.AutoField(primary_key=True, verbose_name='ID')
   publisher = models.CharField(max_length = 50, verbose_name='Publisher')
   author = models.CharField(max_length = 50, verbose_name='Author')
   title = models.CharField(max_length = 100, verbose_name='Title')
   pageCount= models.IntegerField(default=10, verbose_name='Page Count')
   category = models.CharField(max_length = 50, verbose_name='Category')
   shelfLocation = models.CharField(max_length = 50, verbose_name='Shelf Location')
   publishedDate = models.DateField(verbose_name='Published Date')
   isInStock = models.BooleanField(default=True, verbose_name='is in stock')
   dateCheckedOut = models.DateField(verbose_name='Date Checked Out', auto_now=True)

   def __str__(self):
    return f"{self.publisher} {self.author}"