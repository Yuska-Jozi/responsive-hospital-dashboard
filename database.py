from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STR']

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_kpis_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM KPIs"))  
    kpis = []  
    for kpi_row in result:
      kpis.append(kpi_row._asdict())
    return kpis  