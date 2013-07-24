# TitleCase Plugin for Pelican

Pelican blogging framework port of Stuart Colville's titlecase (based on original 
titlecase.pl by John Gruber of www.daringfireball.net)

## What it does

This plugin / jinja filter will convert any text into "Title Case" format. It doesn't simply uppercase each letter of a word, but instead contains logic for proper formatting, when to uppercase, articles, URL's. For more information, refer to the [Daring Fireball article on Title Case](http://daringfireball.net/2008/05/title_case).

An example (an article title)

**Pre-Title Case:**

	Apple profit falls 22% but beats gloomy expectations
	
**Post-Title Case:**

	Apple Profit Falls 22% but Beats Gloomy Expectations

## Installation

1. Clone this repository into where you normally keep your pelican plugins
2. Tell Pelican to use the plugin by modifying your ``pelicanconf.py`` file, and modify
(or add) the ``PLUGINS`` setting:

	``PLUGINS = ["pelican-titlecase"]``

## Usage

Anywhere in your theme's templates, invoke the filter as follows:

	{{ article.title | titlecase }} # This will titlecase all your article titles
