Django Evade
************

|Build status|_

.. |Build status| image::
   https://api.travis-ci.org/richardcornish/django-evade.svg
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

`Full documentation <https://django-evade.readthedocs.io/>`_ is available.

Tests
=====

`Continuous integration test results <https://travis-ci.org/richardcornish/django-evade>`_ are available.