import logging
import threading

from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from apps.email.models import EmailTemplate

logger = logging.getLogger('roomit')


def send_email(template_mnemonic, to):
    template = EmailTemplate.objects.get(mnemonic=template_mnemonic)

    email = EmailMultiAlternatives(template.subject, template.text_content,
                                   settings.EMAIL_HOST_USER, [to])
    email.attach_alternative(template.html_content, 'text/html')
    logger.info('Sending email <{}>, to <{}>, subject: <{}>'.format(template_mnemonic, to, template.subject))
    threading.Thread(target=email.send).start()
