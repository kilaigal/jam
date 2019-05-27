====
Jam
====

Let's make music.

Setup
-----

.. code-block:: console

  git clone https://github.com/kilaigal/jam.git
  cd jam
  tox -e jam

If :code:`tox` is missing, run :code:`pip install tox`


Virtual Environment
------------------

.. code-block:: console

    source .venv/bin/activate
    .venv\Scripts/activate  # Windows


Dependencies
------------

Add package level dependencies to :code:`jam/<package_name>/requirements` and re-run :code:`tox -e jam` to compile and install
