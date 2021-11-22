Django Evade
************

|PyPI version|_ |Build status|_ |Documentation status|_

.. |PyPI version| image::
   https://badge.fury.io/py/django-evade.svg
.. _PyPI version: https://pypi.org/project/django-evade/

.. |Build status| image::
   https://github.com/richardcornish/django-evade/actions/workflows/main.yml/badge.svg
.. _Build status: https://github.com/richardcornish/django-evade/actions/workflows/main.yml

.. |Documentation status| image::
   https://readthedocs.org/projects/django-evade/badge/?version=latest
.. _Documentation status: https://django-evade.readthedocs.io/en/latest/?badge=latest

**Django Evade** is a `Django <https://www.djangoproject.com/>`_ `template filter <https://docs.djangoproject.com/en/dev/howto/custom-template-tags/>`_ application to pseudo-randomly convert literal HTML characters into equivalent `named <https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references>`_, `numeric, or hexadecimal <https://en.wikipedia.org/wiki/Numeric_character_reference>`_ HTML character entity references.

Useful for obscuring ``mailto`` hyperlinks to prevent spammers from collecting e-mail addresses. Inspired by a `Django snippet <https://djangosnippets.org/snippets/216/>`_, but rewritten to use the `Format Specification Mini-Language <https://docs.python.org/3/library/string.html#formatspec>`_. The result is a more severe form of |escape|_, leading to the name "evade."

.. |escape| replace:: ``escape``
.. _escape: https://docs.djangoproject.com/en/dev/ref/templates/builtins/#escape

* `Package <https://pypi.org/project/django-evade/>`_
* `Source <https://github.com/richardcornish/django-evade>`_
* `Documentation <https://django-evade.readthedocs.io/>`_
* `Tests <https://github.com/richardcornish/django-evade/actions/workflows/main.yml>`_

Install
=======

.. code-block:: bash

   $ pip install django-evade

Add to ``settings.py``.

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       "evade",
   ]

Usage
=====

.. code-block:: django

   {% load evade_tags %}

   {{ "me@example.com"|evade }}

One possible result:

.. code-block:: html

   &#x006D;&#x065;&commat;&#x65;&#x78;&#x61;&#x6d;&#112;&#x6C;&#x65;&period;&#x63;&#111;&#x6D;

Note the use of named (``&commat;``), decimal (``&#112;``), hexadecimal lowercase (``&#x6d;``), and hexadecimal uppercase (``&#x6C;``) forms, and the varying length of zero fills (``&#x006D;``, ``&#x065;``). Each character entity reference is pseudo-randomized.

Can also be imported as a standalone Python module:

.. code-block:: python

   >>> from evade import evade
   >>> evade("©")
   '&copy;'
   >>> evade("©")
   '&#169;'
   >>> evade("©")
   '&#x0a9;'
