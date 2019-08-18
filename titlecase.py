# -*- coding: utf-8 -*-
"""
Leverage Python Titlecase pip with Pelican
titlecase @ PyPi: https://pypi.org/project/titlecase/

Authored by Jean-Ray Arseneau
August 2019
"""

from pelican import signals
from titlecase import titlecase

def add_filter(pelican):
    """Add titlecase filter to Pelican."""
    pelican.env.filters.update({'titlecase': titlecase})

def register():
    """Plugin registration."""
    print("Registering Pelican Titlecase Plugin by Jean-Ray Arseneau (https://theint.net/)")
    signals.generator_init.connect(add_filter)

