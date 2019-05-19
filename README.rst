====
Flap
====

Setup
-----

.. code-block:: console

  git clone https://github.com/kilaigal/flap.git
  cd flap
  tox -e flap

If :code:`tox` is missing, run :code:`pip install tox`


Virtual Environment
------------------

.. code-block:: console

    source .venv/bin/activate
    .venv\Scripts/activate  # Windows


Dependencies
------------

Add package level dependencies to :code:`flap/<package_name>/requirements` and re-run :code:`tox -e flap` to compile and install
