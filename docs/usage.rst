.. _usage:

Usage
*****

HTML
====

Load the template tag in a template. Run the filter on a literal or a variable.

.. code-block:: django

   {% extends "base.html" %}

   {% load evade_tags %}

   {% block content %}

       <h1>Contact</h1>

       <p>{{ "me@example.com"|evade }}</p>

       <p><a href="mailto:{{ "me@example.com"|evade }}">{{ "me@example.com"|evade }}</a></p>

       <p>
       {% filter evade %}
       {{ "me@example.com"|evade }}
       {% endfilter %}
       </p>

   {% endblock %}

Python
======

Can also be imported as a standalone Python module:

.. code-block:: python

   >>> from evade import evade
   >>> evade("©")
   '&copy;'
   >>> evade("©")
   '&#169;'
   >>> evade("©")
   '&#x0a9;'
