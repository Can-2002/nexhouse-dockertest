"""Verify installed tools and the database without creating a Django project."""

import os
import platform

import django
import psycopg

print(f"Python {platform.python_version()}")
print(f"Django {django.get_version()} installiert (kein Projekt angelegt)")

with psycopg.connect(
    dbname=os.environ["POSTGRES_DB"],
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    host=os.environ.get("POSTGRES_HOST", "db"),
    port=os.environ.get("POSTGRES_PORT", "5432"),
    connect_timeout=10,
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT version()")
        print(cursor.fetchone()[0])

print("Entwicklungsumgebung bereit. Datenbankverbindung erfolgreich.")
