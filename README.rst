====================
django-iron-sessions
====================

:Info: `iron.io <http://www.iron.io/>`_ cache backend for your Django sessions

Why new sessions backend with non free solution?!
-------------------------------------------------

Why not! `iron.io <http://www.iron.io/>`_ is great service with
awesome live support :)

`iron.io <http://www.iron.io/>`_ provides 100mb and 10M API requests
per month for free


10 000 000 / 30 / 24 / 60 / 60 it's about 4 requests per seconds
with 24/7 loading for your Django appliction

quick start
-----------

run::

    heroku addons:add iron_cache:developer

    pip install django-iron-sessions

configure set ``iron_sessions.session`` as your session engine::

    SESSION_ENGINE = 'iron_sessions.session'

options::

    IRON_CACHE_PROJECT_ID=<YOUR_PROJECT_ID>
    IRON_CACHE_TOKEN=<YOUR_TOKEN>

*if you are on heroku, just skip it*

tests::

    export IRON_CACHE_PROJECT_ID=<YOUR_PROJECT_ID>

    export IRON_CACHE_TOKEN=<YOUR_TOKEN>
    tox

*Python 3.2+ Django 1.5+ ready,
but currently iron_core and iron_cache have some issues with Python 3*
