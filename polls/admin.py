from django.contrib import admin

# Register your models here.
from .models import IdentificationDocument,Study,MaritalStatus,User

admin.site.register(IdentificationDocument)
admin.site.register(Study)
admin.site.register(MaritalStatus)
admin.site.register(User)

