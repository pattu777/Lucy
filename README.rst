.. figure:: https://knowledgeme.s3.amazonaws.com/uploads/collection/background_image/43/cover_step3.jpg
   :alt: 

Lucy
====

A CLI tool to generate ``license`` file for your project.

.. figure:: http://i.imgur.com/ttyy7nk.gif?1
   :alt: 

    **Features**

    -  Written in simple Python
    -  Easy to
       `install <https://github.com/pattu777/Lucy#installation>`__
    -  `Easy to use <https://github.com/pattu777/Lucy#usage>`__
    -  Uses Github v3 API to create your
       ```license`` <https://github.com/karan/joe#list-all-available-files>`__
       file.

Python libraries used
---------------------

-  `Click <http://click.pocoo.org/5/>`__
-  `requests <http://docs.python-requests.org/en/latest/user/quickstart/>`__

Installation
------------

Option 1: via `Pip <https://pypi.python.org/pypi/Lucy>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ pip install lucy

Option 2: From source
~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ git clone --recursive git@github.com:pattu777/Lucy.git
    $ cd Lucy/
    $ python setup.py install

Usage
-----

List all available licenses
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ lucy list

Output:

.. code:: bash

    mit
    mpl-2.0
    gpl-3.0
    lgpl-3.0
    unlicense
    bsd-2-clause
    isc
    lgpl-2.1
    gpl-2.0
    apache-2.0
    cc0-1.0
    artistic-2.0
    bsd-3-clause
    agpl-3.0
    epl-1.0

Generate a new license.
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ lucy create <License Name> --name=<Author Name>             
    $ lucy create mit --name=Chinmaya                     # Creates a MIT license for your project.

Contributing
------------

Bug Reports & Feature Requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Report any bugs through the `issue
tracker <https://github.com/pattu777/Lucy/issues>`__.

Developing
^^^^^^^^^^

Create a new branch and send a pull request. To begin developing, do
this:

.. code:: bash

    # Create a virtual environment
    $ git clone --recursive git@github.com:pattu777/Lucy.git
    $ cd Lucy
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ git checkout -b <feature-branch-name>
    $ python lucy/lucy.py list

