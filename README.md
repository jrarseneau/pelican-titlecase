# TitleCase Plugin for Pelican

Pelican blogging framework port of Stuart Colville's titlecase (based on original 
titlecase.pl by John Gruber of www.daringfireball.net)

## Installation

1. Clone this repository into where you normally keep your pelican plugins
2. Tell Pelican to use the plugin by modifying your ``pelicanconf.py`` file, and modifying
(or adding) the ``PLUGINS`` setting:

	``PLUGINS = ["pelican-titlecase"]``

## Usage

Anywhere in your theme's templates, invoke the filter as follows:

	{{ article.title | titlecase }} # This will titlecase all your article titles
