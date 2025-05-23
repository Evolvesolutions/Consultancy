from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class careerApplication(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')

    def _str_(self):
     return f'{self.fullname} - {self.position}'  # ✅
