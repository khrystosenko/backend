from django.db import models


class EmailTemplate(models.Model):
    mnemonic = models.CharField(max_length=128)
    subject = models.CharField(max_length=128)
    text_content = models.TextField()
    html_content = models.TextField()

    def __str__(self):
        return self.mnemonic

