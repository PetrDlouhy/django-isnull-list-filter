=============================
Django isNull list_filter
=============================

.. image:: https://badge.fury.io/py/django-isnull-list-filter.svg
    :target: https://badge.fury.io/py/django-isnull-list-filter

.. image:: https://travis-ci.org/petrdlouhy/django-isnull-list-filter.svg?branch=master
    :target: https://travis-ci.org/petrdlouhy/django-isnull-list-filter

.. image:: https://codecov.io/gh/petrdlouhy/django-isnull-list-filter/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/petrdlouhy/django-isnull-list-filter

Simple list_filter that offers filtering by __isnull or by blank char field.

Read before using this app
--------------------------

Starting with Django 3.1 the ``EmptyFieldListFilter`` class was embedded: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/filters/#using-a-field-name-and-an-explicit-fieldlistfilter

It has very similar purpose as this app, although it might be little bit lest configurable.
Consider using plain Django before using this app.


Documentation
-------------

The full documentation is at https://django-isnull-list-filter.readthedocs.io.

Quickstart
----------

Install django-isnull-list-filter::

    pip install django-isnull-list-filter

or use development version::

    pip install -e git+https://github.com/PetrDlouhy/django-isnull-list-filter#egg=django-isnull-list-filter

Directly use it in your admin:

.. code-block:: python

    from isnull_filter import isnull_filter
      class MyAdmin(admin.ModelAdmin):
         list_filter = (
             isnull_filter('author'),  # Just set the field
             isnull_filter('author', _("Hasn't got author")),  # Or you can override the default filter title
             isnull_filter('author', _("Has got author"), negate=True),  # And you can negate the condition
         )

or:

.. code-block:: python

    from isnull_filter import isblank_filter
      class MyAdmin(admin.ModelAdmin):
         list_filter = (
             isblank_filter('author'),  # Just set the field
             isblank_filter('author', _("Hasn't got author")),  # Or you can override the default filter title
             isblank_filter('author', _("Has got author"), negate=True),  # And you can negate the condition
         )

Features
--------

* Can be used on:
    * simple field
    * `ForeignKeyField`
    * related `ForeignKeyField`
    * `ManyToManyField`
    * `OneToOneField`
* Default title can be overriden

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Author:

* Petr Dlouhý

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
