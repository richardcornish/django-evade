.. _index:
.. module:: evade

Django Evade
************

|PyPI version|_ |Build status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-evade.svg
.. _PyPI version: https://pypi.python.org/pypi/django-evade

.. |Build status| image::
   https://travis-ci.org/richardcornish/django-evade.svg?branch=master
.. _Build status: https://travis-ci.org/richardcornish/django-evade

**Django Evade** is a `Django <https://www.djangoproject.com/>`_ template filter <https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/>`_ application for numerically escaping characters in templates.

It's just like |escape|_, but forces every character to be escaped randomly into either a `decimal or hexadecimal numeric character reference <https://en.wikipedia.org/wiki/Numeric_character_reference>`_ by using a combination of `Unicode conversion <https://docs.python.org/3/library/functions.html#ord>`_ and `string formatting <https://docs.python.org/3/library/string.html#format-specification-mini-language>`_. Useful for obscuring ``mailto`` hyperlinks to prevent spammers from collecting email addresses. Inspired by a `Django snippet <https://djangosnippets.org/snippets/216/>`_.

.. |escape| replace:: ``escape``
.. _escape: https://docs.djangoproject.com/en/1.11/ref/templates/builtins/#escape

"Evade" sounded like a more severe form of "escape."

* `Package distribution <https://pypi.python.org/pypi/django-evade>`_
* `Code repository <https://github.com/richardcornish/django-evade>`_
* `Documentation <https://django-evade.readthedocs.io/>`_
* `Tests <https://travis-ci.org/richardcornish/django-evade>`_

Install
=======

.. code-block:: bash

   $ pip install django-evade

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       'evade',
   ]

Usage
=====

.. code-block:: django

   {% load evade_tags %}

   {{ "me@example.com"|evade }}

One possible result:

.. code-block:: html

   &#x6d;&#101;&#64;&#x65;&#120;&#x61;&#109;&#x70;&#108;&#101;&#x2e;&#x63;&#111;&#109;

Contents
========

.. toctree::
   :maxdepth: 2

   install
   usage
   documentation
   tests


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
