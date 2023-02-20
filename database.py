from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
    'ssl': {
      'ssl_ca': '/etc/ssl/cert.pem'
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
      #the line above is working because in the tutorial the     
      #teacher uses dict(row) and this command causes a error:
      #TypeError: cannot convert dictionary update sequence 
      #element #0 to a sequence
    return jobs

  
  