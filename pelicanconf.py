#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tadek Teleżyński'
SITENAME = 'blog'
SITEURL = 'https://tadeoos.github.io'
SITELOGO =  '/images/t.gif'

SITESUBTITLE = 'I am computer science student'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR




PATH = 'content'
# STATIC_PATHS = ['images']
# PAGE_PATHS = ['pages']

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('About', ''),)

# Social widget
SOCIAL = (('github', 'http://github.com/tadeoos'),
          ('twitter', 'http://twitter.com/tdkte'),
        #   ('keybase', 'http://keybase.io/tadeo'),
          ('envelope-o', 'mailto:tadekte@gmail.com'),
          )

MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#THEME
THEME = "./Flex"

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'theme/custom.css'
