from html import unescape

from django.template import Context, Template
from django.test import TestCase


class EvadeTestCase(TestCase):
    def test_a(self):
        char = "a"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_1(self):
        char = "1"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_at(self):
        char = "@"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_period(self):
        char = "."
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_ampersand(self):
        char = "&"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_aacute_lower(self):
        char = "á"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_aacute_upper(self):
        char = "Á"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_copyright(self):
        char = "©"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_japanese(self):
        char = "天"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_emoji(self):
        char = "👏"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)

    def test_email(self):
        char = "me@example.com"
        out = Template("{% load evade_tags %}" "{{ char|evade }}").render(
            Context({"char": char})
        )
        self.assertEqual(unescape(out), char)
