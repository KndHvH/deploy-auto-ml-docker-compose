import psycopg2

from os import getenv as env


def get_connection():
    url = env("DATABASE_URL")
    name = env("DATABASE_NAME")
    user = env("DATABASE_USER")
    password = env("DATABASE_PASSWORD")
    port = env("DATABASE_PORT")

    return  psycopg2.connect(f"host={url} dbname={name} user={user} password={password} port={port}")