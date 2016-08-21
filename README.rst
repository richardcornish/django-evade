Django Evade
============

|Build status|_

.. |Build status| image::
   https://secure.travis-ci.org/richardcornish/django-evade.png
.. _Build status: https://travis-ci.org/richardcornish/django-evade

**Django Evade** is a Django template filter application for numerically escaping characters in templates.

Install
=======

Install it with the `pip`<https://pip.pypa.io/en/stable/>_ package manager.

.. code-block:: bash

   mkvirtualenv myvenv -p /usr/local/bin/python3
   pip install django
   pip install -e git+https://github.com/richardcornish/django-evade.git#egg=django-evade

Remember to update your ``requirements.txt`` file. In your project directory:

.. code-block:: bash

   pip freeze > requirements.txt

Usage
=====

Load the template tag in your template. Run it on a variable:

.. code-block:: html

   {% load evade_tags %}

   {{ "me@example.com"|evade }}

   <a href="mailto:{{ "me@example.com"|evade }}">{{ "me@example.com"|evade }}</a>

   {% filter evade %}
   <a href="mailto:me@example.com">me@example.com</a>
   {% endfilter %}