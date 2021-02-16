import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'firsthomework.settings'

if __name__ == '__main__':   

    send_mail(
        'test mail from server',
        'Hello World!',
        'ece568server@163.com',
        ['ys303@duke.edu'],
    )
