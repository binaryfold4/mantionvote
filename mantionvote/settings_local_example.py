# Rename to settings_local.py and customise

SECRET_KEY = 'MustBeUniquePleaseChange'
SOCIAL_AUTH_SOUNDCLOUD_KEY = ''
SOCIAL_AUTH_SOUNDCLOUD_SECRET = ''

DEBUG = False
ALLOWED_HOSTS = [ 'domain.name.here' ]

# comment this out to use default sqlite database (not in production)
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     '',
        'USER':     '',
        'PASSWORD': '',
    }
}

ADMINS = (
	 ('Ryan Verner', 'ryan.verner@gmail.com'),
)

