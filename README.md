#django soundcloud voting tool (API scraper, voting backend)
####Very much a WIP; thar be dragons
####Ryan Verner, 2014 <ryan.verner@gmail.com>

###Requires:

  * Python 3.3+

###Installation:

```bash
pyvenv env
source env/bin/activate
pip install -r requirements.txt
```

###Using:

(If running in production, configure a real DB first in settings.py)

```bash
source env/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py scrape
python manage.py runserver
```

