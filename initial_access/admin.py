from django.contrib import admin
from .models import initaccess
from .models import privescalation
from .models import credentialaccess
from .models import commandcontrol
from .models import execution
from .models import collections
from .models import impact
# Register your models here.
admin.site.register(initaccess)
admin.site.register(privescalation)
admin.site.register(credentialaccess)
admin.site.register(commandcontrol)
admin.site.register(execution)
admin.site.register(collections)
admin.site.register(impact)
