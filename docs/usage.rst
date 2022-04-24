.. _usage:

Usage
*****

HTML
====

Load the template tag in a template. Run the filter on a literal or a variable.

Literal examples:

.. code-block:: django

   {% load evade_tags %}

   <h1>Contact</h1>

   <address>{{ "me@example.com"|evade }}</address>

   <address><a href="{{ "mailto:me@example.com"|evade }}">{{ "me@example.com"|evade }}</a></address>

   <address><a href="{{ "mailto:me@example.com"|evade }}{{ "?subject="|evade }}{{ "Hello, world! How are you?"|urlencode|evade }}">{{ "me@example.com"|evade }}</a></address>

Variable examples:

.. code-block:: django

   {% load evade_tags %}

   <h1>Contact</h1>

   {% if user.is_authenticated and user.email %}
       <address>{{ user.email|evade }}</address>
   {% endif %}

   {% if user.is_authenticated and user.email %}
       <address><a href="{{ "mailto:"|evade }}{{ user.email|evade }}">{{ user.email|evade }}</a></address>
   {% endif %}

   {% if user.is_authenticated and user.email %}
       <address><a href="{{ "mailto:"|evade }}{{ user.email|evade }}{{ "?subject="|evade }}{{ "Hello, world! How are you?"|urlencode|evade }}">{{ user.email|evade }}</a></address>
   {% endif %}

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
