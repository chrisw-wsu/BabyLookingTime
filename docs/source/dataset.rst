=======
Dataset
=======

Contact the authors to gain access to the dataset.

The folder ``students_data`` is shared via One Drive to the team members working on this project.

After cloning this repository on your local machine, make sure to add the shared folder ``students_data`` in the following path:

``student_pathway_project/students_data/``

Any changes to the data must reflect upon the dataset in this folder which is a shared folder with team members.

The dataset consists of the following file structure::

    ├───2015
    │       enrolments2015.csv
    │       offers2015.csv
    │       results2015.csv
    │
    ├───2016
    │       enrolments2016.csv
    │       results2016.csv
    │
    ├───2017
    │       enrolments2017.csv
    │       offers2017.csv
    │       preferences2017.csv
    │       results2017.csv
    │
    ├───2018
    │       enrolments2018.csv
    │       offers2018.csv
    │       preferences2018.csv
    │       results2018.csv
    │
    ├───2019
    │       enrolments2019.csv
    │       offers2019.csv
    │       preferences2019.csv
    │       results2019.csv
    │
    └───combined_data
            final_data.csv



Any cleaning operation must result in storing the ``final_data`` in ``students_data/combined_data/final_data.csv``.

After importing the ``final_data.csv`` file into a Jupyter notebook, make sure to convert the dates into a datetime object.

Example:

``final_data['outcome_date'] = pd.to_datetime(final_data.outcome_date)``

**DO NOT EDIT THE RAW DATA MANUALLY WITH EXCEL OR WITH TEXT EDITOR.**

The key data of interest is **Enrolments** and **Results**.

**EXAMPLE**:

* Enrolments data in 2015 => ``students_data/2015/enrolments2015.csv``
* Results data in 2015 => ``students_data/2015/results2015.csv``
