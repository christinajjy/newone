from django.db import models
    
class initaccess(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200,default='yes')
    option_B=models.CharField(max_length=200,default='no')

    def __str__(self):
        return self.question_id
    

class privescalation(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200)
    option_B=models.CharField(max_length=200)
    option_C=models.CharField(max_length=200)
    option_D=models.CharField(max_length=200)
    keywords=models.TextField(blank=True)

    def __str__(self):
        return self.question_id
    
class credentialaccess(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200)
    option_B=models.CharField(max_length=200)
    option_C=models.CharField(max_length=200)
    option_D=models.CharField(max_length=200)
    keywords=models.TextField(blank=True)

    def __str__(self):
        return self.question_id
    
class commandcontrol(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200)
    option_B=models.CharField(max_length=200)
    option_C=models.CharField(max_length=200)
    option_D=models.CharField(max_length=200)
    keywords=models.TextField(blank=True)

    def __str__(self):
        return self.question_id