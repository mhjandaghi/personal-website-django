from django.db import models

# Create your models here.
class Footer(models.Model):

    address = models.CharField(max_length= 100)
    city = models.CharField(max_length= 30)
    phone = models.CharField(max_length= 14)
    mail = models.EmailField()
    whatsapp = models.CharField(max_length= 50)
    instagram = models.CharField(max_length= 50)
    telegram = models.CharField(max_length= 50)

    
class Ticket(models.Model):
    name = models.CharField(max_length=80)
    mail = models.EmailField(default = 'a', blank=True)
    subject = models.CharField(max_length=80)
    text = models.TextField()
    phone = models.CharField(max_length=15, default=0)


    def __str__(self) -> str:
        return f'{self.subject} : {self.name}'
    