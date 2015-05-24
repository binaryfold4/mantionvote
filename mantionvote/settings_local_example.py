# Rename to settings_local.py and customise

SECRET_KEY = 'MustBeUniquePleaseChange'
SOCIAL_AUTH_SOUNDCLOUD_KEY = ''
SOCIAL_AUTH_SOUNDCLOUD_SECRET = ''

DEBUG = False
ALLOWED_HOSTS = [ 'domain.name.here' ]

# if running local development: you can comment this out (will use sqlite)
# you will need to "pip install mysqlclient" (not installed by default, see requirements.txt)
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

# for production only: set below to /static directory you configure nginx to serve from
STATIC_ROOT=""