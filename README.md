HypemFinderSite
===============

A website to help people download songs from Hypem.com!

Installation
============

1. Download setuptools (easy_install)
2. Use easy_install to install pip
3. Use pip to install virtualenv
4. Create a virtualenv and activate it
5. Use pip to install dependencies based on requirements.txt file


Launching Site Devo
====================
1.  python .\manage.py collectstatic --settings=mysite.settings.dev
2.  python .\manage.py runserver --settings=mysite.settings.dev
3.  http://127.0.0.1:8000/hypemfinder/

Launching Site Prod
===================
1. install mod_wsgi for apache2. (sudo apt-get install libapache2-mod-wsgi)
2. create an application directory under your domain directory (sudo mkdir ~/public/<DOMAIN>/application)
3. change to that application directory
4. git pull your django application inside!
5. change the grp to www-data (sudo chgrp -r www-data *)
6. create virtualenv (virtualenv env)
7. activate environment (source env/bin/activate)
8. pip install -r requirements.txt


MIGRATIONS
=============
$./manage.py schemamigration hypemfinder --auto
-> This will create the migration python file
$./manage.py migrate hypemfinder
->With that the new columns are migrated!
