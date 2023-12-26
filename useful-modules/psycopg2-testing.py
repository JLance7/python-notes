import psycopg2
from urllib.parse import urlparse
from sqlalchemy import create_engine


def get_conn_str(username: str, password: str, host: str, port: str, database: str):
  conn_str = f"postgresql://{username}:{password}@{host}:{port}/{database}"
  return conn_str


def create_conn(conn_str: str) -> str:
  result = urlparse(conn_str)
  username = result.username
  password = result.password
  host = result.hostname
  port = result.port
  database = result.path[1:]

  conn = psycopg2.connect(
      dbname=database,
      user=username,
      password=password,
      host=host,
      port=port,
  )
  return conn


def create_db_engine(conn_str):
  db_engine = create_engine(conn_str)
  return db_engine


def run_sql(conn, sql):
  cur = conn.curosr()
  cur.execute(sql)
  cur.close()
  conn.commit()


def df_to_sql(df, db_engine, schema, table, append):
  df.to_sql(
    name=table,
    con=db_engine,
    schema=schema,
    if_exists=append,
    index=False
  )