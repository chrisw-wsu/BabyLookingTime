===============
Data Processing
===============

All the operation related to data processing must be performed in `data_processing.ipynb`.

**DO NOT LEAVE ANY DATA VISIBLE ON JUPYTER NOTEBOOK BEFORE COMMITING**.

The code is developed to automatically collect data from a `.csv` to **Pandas** dataframe.

The data from each year is stored in an array of dataframe and then merged together as a single dataframe.

The primary key in `results` and `enrolments` data is the `student_id`.

The `student_id` is used to merge the demographic data from `enrolments` and the unit outcome from `results`.

The `final_data` is generated which is a combination of all the years of data.
