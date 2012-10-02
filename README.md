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


Launching Site
==============
1.  python .\manage.py collectstatic --settings=mysite.settings.dev
2.  python .\manage.py runserver --settings=mysite.settings.dev
3.  http://127.0.0.1:8000/hypemfinder/