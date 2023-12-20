from django.contrib import admin
from .models import initaccess
from .models import privescalation
from .models import credentialaccess
from .models import commandcontrol
# Register your models here.
admin.site.register(initaccess)
admin.site.register(privescalation)
admin.site.register(credentialaccess)
admin.site.register(commandcontrol)
