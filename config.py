import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = '!@#secure!@#Key321'

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'webstore1092@gmail.com'
MAIL_PASSWORD = 'test123456789'
ADMINS = ['webstore1092@gmail.com']

try:
    from local_config import *
except ImportError:
    pass

