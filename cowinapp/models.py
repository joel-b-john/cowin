from django.db import models

# Create your models here.
class Slot(models.Model):
    name=models.CharField(max_length=250)
    number=models.IntegerField()
    date=models.DateTimeField()
    vaccine=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    token=models.IntegerField()


    class Meta:
        ordering=('name',)
        verbose_name='slot'
        verbose_name_plural='slots'

    def __str__(self):
        return '{}'.format(self.name)
class Token (models.Model):
    tk=models.IntegerField()
