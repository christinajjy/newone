from django.db import models
    
class initaccess(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200,default='yes')
    option_B=models.CharField(max_length=200,default='no')
    keywords=models.TextField(blank=True)

    def __str__(self):
        return self.question_id
    

class privescalation(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200,default='yes')
    option_B=models.CharField(max_length=200,default='no')
    keywords=models.TextField(blank=True)

    def __str__(self):
        return self.question_id
    
class credentialaccess(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200,default='yes')
    option_B=models.CharField(max_length=200,default='no')
    keywords=models.TextField(blank=True)

    def __str__(self):
        return self.question_id
    
class commandcontrol(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200,default='yes')
    option_B=models.CharField(max_length=200,default='no')
    keywords=models.TextField(blank=True)

    def __str__(self):
        return self.question_id

    
class execution(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200,default='yes')
    option_B=models.CharField(max_length=200,default='no')
    keywords=models.TextField(blank=True)
    def __str__(self):
        return self.question_id
class collections(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200,default='yes')
    option_B=models.CharField(max_length=200,default='no')
    keywords=models.TextField(blank=True)
    def __str__(self):
        return self.question_id
class impact(models.Model):
    question_id = models.CharField(max_length=200)
    question=models.TextField(blank=True)
    option_A=models.CharField(max_length=200,default='yes')
    option_B=models.CharField(max_length=200,default='no')
    keywords=models.TextField(blank=True)
    def __str__(self):
        return self.question_id




# class responses(models.Model):
#     session_id = models.IntegerField()
#     initial_access_result = models.IntegerField()
#     privescalation_result = models.IntegerField()
#     credentialaccess_result = models.IntegerField()
#     commandcontrol_result = models.IntegerField()

#     def __str__(self):
#         return self.session_id