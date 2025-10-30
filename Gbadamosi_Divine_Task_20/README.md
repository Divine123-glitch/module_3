# Library Database Management — Setup and Run Guide

This folder contains a Library Database Management assignment with SQL scripts, Python helpers, and Jupyter notebooks for analysis and visualization.

This README explains how to set up the environment, install dependencies, create the PostgreSQL database and tables, load data, run the Python scripts, and open the notebooks on Windows (PowerShell). Commands in the "Try it" sections are written for PowerShell.

## Contents

- `Sql_scripts/` — SQL files to create tables, load data, and queries.
- `python_scripts/` — Python helpers including `database_connection.py` and notebooks.
- `Screenshots/` — Example outputs and screenshots used for deliverables.
- `requirements.txt` — Python dependencies.

## Prerequisites

- Windows with PowerShell (this repo was prepared on Windows).
- Python 3.8+ installed and on PATH.
- PostgreSQL server (12+) installed locally or accessible remotely.
- Optional: VS Code with the PostgreSQL and Python extensions for convenience.

## 1) Create a Python virtual environment and install dependencies

Open PowerShell in the project root (the folder that contains this README) and run:

```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Note: `requirements.txt` includes SQLAlchemy and `psycopg2-binary` for PostgreSQL connectivity.

## 2) PostgreSQL: create database and user

If you have PostgreSQL installed locally, create the database `library_db` and a user for the project. Replace `myuser` and `mypassword` with your chosen credentials.

```powershell
# From psql shell (example):
# psql -U postgres

# Example SQL to run inside psql:
CREATE DATABASE library_db;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE library_db TO myuser;
\q
```

If PostgreSQL is not local, use the host, port, user, and password for your server in the steps below.

## 3) Create tables

Open the SQL script `Sql_scripts/01_create_tables.sql` in a SQL client (psql or VS Code PostgreSQL extension) and run it against the `library_db` database. The script contains the table definitions and custom enum types used by the schema.

PowerShell/psql example (adjust path and user):

```powershell
# Run the SQL script using psql (change the path to psql if needed)
psql -U myuser -d library_db -f "Sql_scripts\01_create_tables.sql"
```

If you prefer to run the statements interactively, open a `psql` shell connected to `library_db` and paste the SQL statements from the file.

## 4) Load sample data

Use `Sql_scripts/02_load_data.sql` (if present) to load sample records into the tables. Run it the same way as the create script:

```powershell
psql -U myuser -d library_db -f "Sql_scripts\02_load_data.sql"
```

If you don't have `02_load_data.sql`, insert sample rows manually or with any CSV-import method you prefer. Ensure referential integrity to enact foreign keys: insert authors and departments before books and staff, and members before borrow history.

## 5) Test the database connection from Python

The repository contains `python_scripts\database_connection.py`. It expects the following environment variables:

- `DB_HOST` (e.g., `localhost`)
- `DB_PORT` (optional, default `5432`)
- `DB_NAME` (e.g., `library_db`)
- `DB_USER`
- `DB_PASSWORD`

Example PowerShell one-liner to export env vars and run the script (replace credentials):

```powershell
$env:DB_HOST="localhost"; $env:DB_PORT="5432"; $env:DB_NAME="library_db"; $env:DB_USER="myuser"; $env:DB_PASSWORD="mypassword"; python .\python_scripts\database_connection.py
```

## 6) Using the notebooks and pandas queries

There are two notebooks in `python_scripts/`:
- `part5_pandas_queries.ipynb` — pandas translations of SQL queries
- `part6_visualizations.ipynb` — plotting and visualization code
Open the notebooks in Jupyter. If you don't have Jupyter installed, you can install it in the virtual environment:

```powershell

Quick command to start Jupyter (inside virtual environment):

```powershell
jupyter notebook
```

```

## 7) Deliverables and submission checklist

- `Sql_scripts/01_create_tables.sql` — database schema
- `Sql_scripts/02_load_data.sql` — data loading 
- `Sql_scripts/03_queries.sql` — SQL queries and answers
- `python_scripts/` — `database_connection.py`, notebook files, and any scripts you produce
- `Screenshots/` — screenshots showing successful table creation, data load, and query outputs

Before zipping for submission, I ensure the `README.md` is present and the screenshots are organized into the `Screenshots/` subfolders.

