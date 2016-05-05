from django.contrib import admin
from apps.email.models import EmailTemplate


class EmailTemplateAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmailTemplate, EmailTemplateAdmin)

