============
Contributing
============

We are a small team of four from `Technical Support Services`_ at `Western Sydney University`_, but we would definitely like to expand some day.

.. _Technical Support Services: https://www.westernsydney.edu.au/tss
.. _Western Sydney University: https://www.westernsydney.edu.au/

Types of Contributions
----------------------

Report Bugs
^^^^^^^^^^^

Report bugs at https://github.com/wsu-tss/student_pathway_project/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Submit Feedback
^^^^^^^^^^^^^^^

The best way to send feedback is to file an issue at https://github.com/wsu-tss/student_pathway_project/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

Get started!
------------

1. Follow the instructions in the Installation section to setup the project.

2. Make sure you create virtual environment and install all the dependencies.

3. Makes sure to use the same virtual environment in the Jupyter notebook.

4. To work on a Jupyter notebook:
    a. Create an issue_ based on what you are working on.
    b. Create a Jupyter notebook in the root of the project.
    c. Use Jupyter notebook only for data analysis and data filtering purposes.
    d. If a function becomes repetitive, make sure to create a module inside ``studentpathway``.

5. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

Now, you can make changes locally.

6. Creating modules
    a. If you are adding a new feature which is repetitive and has a scope over the project,
       create a separate python file as a submodule in ``studentpathway`` module.
    b. There are already two submodules ``dataprocessing`` and ``adjacency``.
       If the functionality can be categorised under these two submodules, add the python file inside these submodules.
    c. If there is not specific submodule to the feature, create a different submodule.
    d. When creating a new submodule, create ``__init__.py`` file inside the submodule directory.

7. When you are making changes in the modules, make sure that your changes pass the tests::

    $ python -m pytest

8. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

9. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

* The pull request should include tests.
* If the pull request adds functionality, the docs should be updated.
  Put your new functionality into a function with a docstring, and add the
  feature to the list in README.rst.
* The pull request should work for Python version 3.6 and above.

.. _issue: https://github.com/wsu-tss/student_pathway_project/issues
