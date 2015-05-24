###django soundcloud voting tool (API scraper, voting backend)
Ryan Verner, 2014 <ryan.verner@gmail.com>

*WIP: THAR BE DRAGONS*

####Requires:

  * Python 3.4+ (probably will run on Python 2.7 with some changes)
  * python3.4-venv

####Installation:

```bash
pyvenv-3.4 env
source env/bin/activate
pip install -r requirements.txt
```

####Using:

Copy mantionvote/settings_local_example.py to mantionvote/settings_local.py.
Please populate this with real information (database, secret key, etc).

```bash
source env/bin/activate
python manage.py migrate
python manage.py createsuperuser
python manage.py scrape
python manage.py runserver
```

