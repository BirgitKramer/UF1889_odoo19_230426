import traceback

import psycopg2

def get_connection(dbname):
    return psycopg2.connect(
        host='localhost',
        port=5432,
        user='odoo',
        password='1234',
        dbname=dbname
    )

conn = None
for dbname in ['odoo19', 'odoo', 'postgres']:
    try:
        conn = get_connection(dbname)
        print(f"Conectado a base de datos: {dbname}")
        break
    except Exception as e:
        print(f"Error conectando a {dbname}:")
        print(f"  type: {type(e)}")
        print(f"  str: '{str(e)}'")
        print(f"  repr: '{repr(e)}'")
        print(f"  args: {e.args}")

if conn is None:
    exit(1)
cur = conn.cursor()
cur.execute("SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema NOT IN ('pg_catalog', 'information_schema') ORDER BY table_schema, table_name")
tables = cur.fetchall()

for schema, table in tables:
    print(f"{schema}.{table}")

conn.close()