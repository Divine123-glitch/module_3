"""
database_connection.py
Simple test script to connect to a PostgreSQL database named `library_db`.

Usage:
  - Set environment variables: DB_HOST, DB_PORT (optional), DB_NAME, DB_USER, DB_PASSWORD
  - Run: python database_connection.py

If environment variables are not set, the script prints usage examples and exits.
"""
import os
import sys


def get_env():
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT", "5432")
    db = os.environ.get("DB_NAME")
    user = os.environ.get("DB_USER")
    pwd = os.environ.get("DB_PASSWORD")
    return host, port, db, user, pwd


def print_usage():
    print("No database credentials found in environment.")
    print("Set the following environment variables and re-run:")
    print("  DB_HOST, DB_PORT (optional, default 5432), DB_NAME, DB_USER, DB_PASSWORD")
    print()
    print("PowerShell example (single-line):")
    print('  $env:DB_HOST="localhost"; $env:DB_PORT="5432"; $env:DB_NAME="library_db"; $env:DB_USER="myuser"; $env:DB_PASSWORD="mypassword"; python database_connection.py')
    print()
    print("Or use a SQLAlchemy connection string format:")
    print("  postgresql://myuser:mypassword@localhost:5432/library_db")


def test_with_sqlalchemy(host, port, db, user, pwd):
    try:
        from sqlalchemy import create_engine, text
    except Exception:
        print("SQLAlchemy (or dependencies) not installed. Install with:")
        print("  python -m pip install SQLAlchemy psycopg2-binary")
        return

    url = f"postgresql://{user}:{pwd}@{host}:{port}/{db}"
    safe_url = url.replace(pwd, "****") if pwd else url
    print("Attempting to connect using SQLAlchemy to:", safe_url)
    try:
        engine = create_engine(url, connect_args={"connect_timeout": 5})
        with engine.connect() as conn:
            res = conn.execute(text("SELECT 1"))
            scalar = res.scalar()
            print("Query result:", scalar)
        print("Connection successful.")
    except Exception as e:
        print("Connection failed:", repr(e))


def main():
    host, port, db, user, pwd = get_env()
    if not (host and db and user and pwd):
        print_usage()
        sys.exit(0)
    test_with_sqlalchemy(host, port, db, user, pwd)


if __name__ == "__main__":
    main()

import pandas as pd
from sqlalchemy import create_engine

# Create database connection
engine = create_engine('postgresql://postgres:kanyisola@localhost:5432/library_db')

# Example: Load data
df_books = pd.read_sql("SELECT * FROM Books", engine)
df_authors = pd.read_sql("SELECT * FROM Authors", engine)

df_books.head()

# Your Pandas queries here
