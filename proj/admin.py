from django.contrib import admin
from .models import Account, DataLog, StatusLog, Maintenance

# Register your models here.
admin.site.register(Account)
admin.site.register(DataLog)
admin.site.register(StatusLog)
admin.site.register(Maintenance)