``filesystem`` module
=====================

.. code:: python

    import filesystem as fs

Testing if a path is a file (shortcut for ``try``/``with open``):
-----------------------------------------------------------------

.. code:: python

    fs.isfile('something')
    fs.isfile('something', mode='r')

Shortcut for ``rsync -a``
-------------------------

Uses ```sh`` module <https://pypi.python.org/pypi/sh/>`__.

.. code:: python

    fs.sync('name@somehost:~/somedir/', 'local_path')
    fs.sync('~/somedir', '.')

Returns exit code and does not catch any exceptions raised by ``sh``.

Check if a file is the same based on modified time
--------------------------------------------------

Example use: determine if a file is the same based on a ``HEAD`` HTTP
request using the ``Last-Modified`` header.

.. code:: python

    from urllib2.request import urlopen

    req = urlopen('http://i.imgur.com/sgon5YP.jpg')
    req.get_method = lambda: 'HEAD'
    last_modified = None

    for line in str(req.info()).split('\n'):
        if 'last-modified' in line.lower():
            last_modified = line.split(': ')[1].strip()
            last_modified = time.strptime(last_modified.replace(' GMT', ''), '%a, %d %b %Y %H:%M:%S')
            break

    # Actual check
    fs.has_same_time('./sgon5YP.jpg', last_modified)

Delete a set of files
---------------------

Use ``fs.rm_files(list_of_files, raise_on_error=bool_val)``.

``pushd`` usage with the ``with`` statement
===========================================

.. code:: python

    from osext.pushdcontext import pushd

    with pushd('some_dir') as context:
        pass

