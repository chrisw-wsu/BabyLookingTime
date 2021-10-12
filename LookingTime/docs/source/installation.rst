============
Installation
============


Installing Git
--------------

Download git_ on your computer.

.. _git: https://git-scm.com/


Access to GitHub repository
---------------------------

Contact authors for read and write access to GitHub repository.


Downloading the project repository
----------------------------------

Type the following in the command prompt/terminal::

    $ git clone https://github.com/wsu-tss/student_pathway_project.git

Dataset
-------

Consult the team members to request access to the folder ``students_data``.

Add this folder in the root of this project.


Creating virtual environment and installing the requirements
------------------------------------------------------------

Create a virtual environment and install all the required packages from ``requirements.txt``

Windows instructions
^^^^^^^^^^^^^^^^^^^^

Make sure to download Anaconda Navigator on your computer.

Use Anaconda Powershell and navigate to the project root directory.

Create a virtual environment by typing the following::

    $ conda create --prefix ./venv

Activate virtual environment::

    $ conda activate ./venv

Install dependencies::

    $ conda install --file requirements.txt


MacOS instructions
^^^^^^^^^^^^^^^^^^

Install Virtual Environment package::

    $ pip install virtualenv

Create Virtual Environment::

    $ virtualenv venv

Activate Virtual Environment::

    $ source venv/bin/activate

Install dependencies::

    $ pip install -r requirements.txt

Linux instructions
^^^^^^^^^^^^^^^^^^

Create Virtual Environment::

    $ python -m venv venv

Activate Virtual Environment::

    $ source venv/bin/activate

Install dependencies::

    $ pip install -r requirements.txt


Virtual Environment in Jupyter NOTEBOOK
---------------------------------------

Open Terminal/Anaconda Powershell Prompt and execute the following::

    $ ipython kernel install --user --name=venv

Launch Jupyter notebook from Anaconda Powershell Prompt by executing the following::

    $ jupyter notebook

Changing the kernel in jupyter Notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the menu bar select ``Kernel > Change kernel > venv``.

While creating a new notebook, select ``venv`` instead of ``Python3``.


Possible Errors while installing packages
-----------------------------------------

Issues with installing Tensorflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While working on the Windows OS, if the path of the installation inside the package folder exceeds more than 260 characters,
then the installation will not be complete.

To fix this error refer the following steps:

1. Hit the Windows key, type ``gpedit.msc`` and press Enter.
2. Navigate to ``Local Computer Policy > Computer Configuration > Administrative Templates > System > Filesystem``.
3. Double click the ``Enable Win32 long paths`` option and enable it.

If the option ``Enable Win32 long paths`` is unavailable, change the project location on your local machine
or reduce the character name of the project folder.

This error was encountered while installing ``tensorflow`` module.

Refer the `issue`_

.. _issue: https://github.com/tensorflow/tensorflow/issues/24835
