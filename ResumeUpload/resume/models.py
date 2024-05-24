from django.db import models

STATECHOICE=(('MP','MP'),('UP','UP'),('AP','AP'),('GJ','GJ'))
# Create your models here.
class Resume(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    dob=models.DateField(auto_now=False,auto_now_add=False)
    state=models.CharField(choices=STATECHOICE,max_length=100)
    gender=models.CharField(max_length=20)
    location=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image',blank=True)
    dock=models.FileField(upload_to='dock',blank=True)

    def __str__(self):
        return self.name
