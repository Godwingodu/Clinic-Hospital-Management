from django.db import models


#Patients model
class Patients(models.Model):
    fullname = models.CharField(max_length = 100)
    dob = models.DateField()
    options = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )
    gender = models.CharField(choices = options,max_length = 100,default = "Other")
    contact_number = models.IntegerField()
    address = models.CharField(max_length = 1000)
    medical_condition = models.CharField(max_length = 1000)
    profile_pic = models.ImageField(upload_to = "profile_pictures",null = True,blank = True)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'patient'
        verbose_name_plural = 'patients'
