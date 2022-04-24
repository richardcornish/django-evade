from html import unescape

from django.contrib.auth import get_user_model
from django.template import Context, Template
from django.test import TestCase

User = get_user_model()


class EvadeTestCase(TestCase):
    """Evade test cases."""

    def setUp(self):
        self.user = User.objects.create_user(
            "me", email="me@example.com", password="password"
        )

    def test_a(self):
        out = Template("{% load evade_tags %}" "{{ 'a'|evade }}").render(Context())
        self.assertEqual(unescape(out), "a")

    def test_1_string(self):
        out = Template("{% load evade_tags %}" "{{ '1'|evade }}").render(Context())
        self.assertEqual(unescape(out), "1")

    def test_1_integer(self):
        out = Template("{% load evade_tags %}" "{{ 1|evade }}").render(Context())
        self.assertEqual(unescape(out), "1")

    def test_at(self):
        out = Template("{% load evade_tags %}" '{{ "@"|evade }}').render(Context())
        self.assertEqual(unescape(out), "@")

    def test_period(self):
        out = Template("{% load evade_tags %}" '{{ "."|evade }}').render(Context())
        self.assertEqual(unescape(out), ".")

    def test_ampersand(self):
        out = Template("{% load evade_tags %}" '{{ "&"|evade }}').render(Context())
        self.assertEqual(unescape(out), "&")

    def test_aacute_lower(self):
        out = Template("{% load evade_tags %}" '{{ "á"|evade }}').render(Context())
        self.assertEqual(unescape(out), "á")

    def test_aacute_upper(self):
        out = Template("{% load evade_tags %}" '{{ "Á"|evade }}').render(Context())
        self.assertEqual(unescape(out), "Á")

    def test_copyright(self):
        out = Template("{% load evade_tags %}" '{{ "©"|evade }}').render(Context())
        self.assertEqual(unescape(out), "©")

    def test_japanese(self):
        out = Template("{% load evade_tags %}" '{{ "天"|evade }}').render(Context())
        self.assertEqual(unescape(out), "天")

    def test_emoji(self):
        out = Template("{% load evade_tags %}" '{{ "👏"|evade }}').render(Context())
        self.assertEqual(unescape(out), "👏")

    def test_email(self):
        out = Template("{% load evade_tags %}" '{{ "me@example.com"|evade }}').render(
            Context()
        )
        self.assertEqual(unescape(out), "me@example.com")

    def test_email_mailto(self):
        out = Template(
            "{% load evade_tags %}"
            '<address><a href="{{ "mailto:me@example.com"|evade }}">{{ "me@example.com"|evade }}</a></address>'
        ).render(Context())
        self.assertEqual(
            unescape(out),
            '<address><a href="mailto:me@example.com">me@example.com</a></address>',
        )

    def test_email_mailto_query(self):
        out = Template(
            "{% load evade_tags %}"
            '<address><a href="{{ "mailto:me@example.com"|evade }}{{ "?subject="|evade }}{{ "Hello, world! How are you?"|urlencode|evade }}">{{ "me@example.com"|evade }}</a></address>'
        ).render(Context())
        self.assertEqual(
            unescape(out),
            '<address><a href="mailto:me@example.com?subject=Hello%2C%20world%21%20How%20are%20you%3F">me@example.com</a></address>',
        )

    def test_context_email(self):
        out = Template("{% load evade_tags %}" "{{ string|evade }}").render(
            Context({"string": "me@example.com"})
        )
        self.assertEqual(unescape(out), "me@example.com")

    def test_context_email_mailto(self):
        out = Template(
            "{% load evade_tags %}"
            '<address><a href="{{ "mailto:"|evade }}{{ string|evade }}">{{ string|evade }}</a></address>'
        ).render(Context({"string": "me@example.com"}))
        self.assertEqual(
            unescape(out),
            '<address><a href="mailto:me@example.com">me@example.com</a></address>',
        )

    def test_context_email_mailto_query(self):
        out = Template(
            "{% load evade_tags %}"
            '<address><a href="{{ "mailto:"|evade }}{{ string|evade }}?{% filter evade %}{% for k, v in params.items %}{{ k }}={{ v|urlencode }}{% endfor %}{% endfilter %}">{{ string|evade }}</a></address>'
        ).render(
            Context(
                {
                    "string": "me@example.com",
                    "params": {
                        "subject": "Hello, world! How are you?",
                    },
                }
            )
        )
        self.assertEqual(
            unescape(out),
            '<address><a href="mailto:me@example.com?subject=Hello%2C%20world%21%20How%20are%20you%3F">me@example.com</a></address>',
        )

    def test_context_email_user(self):
        out = Template(
            "{% load evade_tags %}"
            "{% if user.is_authenticated and user.email %}{{ user.email|evade }}{% endif %}"
        ).render(Context({"user": self.user}))
        self.assertEqual(unescape(out), "me@example.com")

    def test_context_email_user_mailto(self):
        out = Template(
            "{% load evade_tags %}"
            '{% if user.is_authenticated and user.email %}<address><a href="{% filter evade %}mailto:{{ user.email }}{% endfilter %}{% endif %}">{{ user.email|evade }}</a></address>'
        ).render(Context({"user": self.user}))
        self.assertEqual(
            unescape(out),
            '<address><a href="mailto:me@example.com">me@example.com</a></address>',
        )
