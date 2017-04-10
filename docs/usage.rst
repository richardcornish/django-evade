.. _usage:

Usage
*****

Load the template tag in a template. Run the filter on a variable.

.. code-block:: django

   {% extends "base.html" %}

   {% load evade_tags %}

   {% block content %}

       <h1>Contact</h1>

       <p>{{ "me@example.com"|evade }}</p>

       <p><a href="mailto:{{ "me@example.com"|evade }}">{{ "me@example.com"|evade }}</a></p>

       {% filter evade %}
       <p><a href="mailto:me@example.com">me@example.com</a></p>
       {% endfilter %}

   {% endblock %}
