Third Party Tangled Extensions
==============================

``tangled.contrib`` is a namespace package for third party Tangled extensions.
The layout for such an extension looks like this::

    ${project root}/
        setup.py
        README
        tangled/ (empty directory)
            contrib/ (empty directory)
                ${package name}/
                    __init__.py

The ``tangled contrib new`` command can be used to create such a package::

    tangled contrib new sqlalchemy

This will create the following directories and files in the directory where the
command was run::

    tangled.contrib.sqlalchemy/
        setup.py
        README
        tangled/
            contrib/
                sqlalchemy/
                    __init__.py

`Documentation <http://tangledframework.org/docs/tangled.contrib/>`_
