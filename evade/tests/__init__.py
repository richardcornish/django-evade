# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.template import Context, Template
from django.test import TestCase


class EvadeTestCase(TestCase):
    """
    Uses assertTrue over assertEqual because returned value can be either character
    https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue
    """
    def test_a(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ 'a'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#97;" or "&#x61;")

    def test_1(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ '1'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#49;" or "&#x31;")

    def test_at(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ '@'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#64;" or "&#x40;")

    def test_period(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ '.'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#46;" or "&#x2e;")

    def test_ampersand(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ '&'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#38;" or "&#x26;")

    def test_hash(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ '#'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#35;" or "&#x23;")

    def test_semicolon(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ ';'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#59;" or "&#x3b;")

    def test_copyright(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ '©'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#169;" or "&#xa9;")

    def test_japanese(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ '食'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#39135;" or "&#x98df;")

    def test_clapping(self):
        out = Template(
            "{% load evade_tags %}"
            "{{ '👏'|evade }}"
        ).render(Context())
        self.assertTrue(out == "&#128079;" or "&#x1f44f;")
