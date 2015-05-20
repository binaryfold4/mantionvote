###django soundcloud voting tool (API scraper, voting backend)
Ryan Verner, 2014 <ryan.verner@gmail.com>

*WIP: THAR BE DRAGONS*

####Requires:

  * Python 3.4+ (probably will run on Python 2.7 with some changes)

####Installation:

```bash
pyvenv env
source env/bin/activate
pip install -r requirements.txt
```

####Using:

(If running in production, configure a real DB first in settings.py)

(Shouldn't be used in production yet anyway)

```bash
source env/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py scrape
python manage.py runserver
```

