Django Evade
************

|Build status|_

.. |Build status| image::
   https://secure.travis-ci.org/richardcornish/django-evade.png
.. _Build status: https://travis-ci.org/richardcornish/django-evade

**Django Evade** is a Django template filter application for numerically escaping characters in templates.

Install
=======

.. code-block:: bash

   pip install -e git+https://github.com/richardcornish/django-evade.git#egg=django-evade

Usage
=====

.. code-block:: html

   {% load evade_tags %}

   {{ "me@example.com"|evade }}

Documentation
=============

`Full documentation <http://django-evade.readthedocs.io/en/latest/>`_ is available.