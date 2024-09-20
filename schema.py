import lib.pgsql as pgsql

DB = pgsql.PgSQL()

# Connect to the PostgreSQL database
try:
    DB.connect()
except Exception as e:
    print('Error connecting to the database')
    print(e)
    exit()


