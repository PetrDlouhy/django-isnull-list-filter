=============================
Django isNull list_filter
=============================

.. image:: https://badge.fury.io/py/django-isnull-list-filter.svg
    :target: https://badge.fury.io/py/django-isnull-list-filter

.. image:: https://travis-ci.org/petrdlouhy/django-isnull-list-filter.svg?branch=master
    :target: https://travis-ci.org/petrdlouhy/django-isnull-list-filter

.. image:: https://codecov.io/gh/petrdlouhy/django-isnull-list-filter/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/petrdlouhy/django-isnull-list-filter

Simple list_filter that offers filtering by __isnull.

Documentation
-------------

The full documentation is at https://django-isnull-list-filter.readthedocs.io.

Quickstart
----------

Install Django isNull list_filter::

    pip install django-isnull-list-filter

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'isnull_filter.apps.IsnullFilterConfig',
        ...
    )

Add Django isNull list_filter's URL patterns:

.. code-block:: python

    from isnull_filter import urls as isnull_filter_urls


    urlpatterns = [
        ...
        url(r'^', include(isnull_filter_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
