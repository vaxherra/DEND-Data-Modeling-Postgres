# Introduction

## Purpose

**To structure and simplify Sparkify's access to user activity.** 

- facilitating queries concerning user activity (songs listened)
- moving from directory of JSON logs into snowflake RDBMS system on PostgreSQL

 
Currently, Sparkify doesn't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

## Goals

- Define STAR-like data structure in PostgreSQL
- Define a set of SQL queries to":
    - drop tables
    - create designed tables (schema)
    - populate tables
- Define a set of scripts for batch processing of gathered `JSON` logs



# Code structure

## Scripts
- `sql_queries.py` - defines schema structure, functions to `DROP` and `UPSERT` into tables
- `create_Tables.py` - a helper function to clear existing schema, and create a blank (empty) structure ready to fill
- `etl.py` - a function to batch-process files on a) `song_data` and b) `log_data` in the provided directory

## Helper notebooks
- `etl.ipynb` - a notebook to document and test the functions inserting data into tables. Notebook works on a single (example) file, and demonstrates/prototypes the functions and processing for the proper upload of data into PostgreSQL

- `test.ipynb` - a notebook to document that the data was properly formatted and uploaded into designed schemas. A set of simple SQL queries to display table structure.



# Database Schema

Overview:

## Fact Table

- `songplays` - records in log data associated with song plays i.e. records with page NextSong
        `songplay_id`, `start_time`, `user_id`, `level`, `song_id`, `artist_id`, `session_id`, `location`, `user_agent`

## Dimension Tables

- `users` - users in the app
    `user_id`, `first_name`, `last_name`, `gender`, `level`
- `songs` - songs in music database
    `song_id`, `title`, `artist_id`, `year`, `duration`
- `artists` - artists in music database
        `artist_id`, `name`, `location`, `latitude`, `longitude`
- `time` - timestamps of records in songplays broken down into specific units
        `start_time`, `hour`, `day`, `week`, `month`, `year`, `weekday`


# Example queries

Please see `test.ipynb` notebooks for example basic queries.

The central "fact" table is `songplays` that could be easily queried to obtain desired information.


