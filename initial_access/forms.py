from django.db import models
from django.forms import ModelForm

class Initial_access(models.Model):
    model = Initial_access_responses
    fields = [option_A,option_B]