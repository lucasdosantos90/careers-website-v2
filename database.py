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
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
      #the line above is working because in the tutorial the     
      #teacher uses dict(row) and this command causes a error:
      #TypeError: cannot convert dictionary update sequence 
      #element #0 to a sequence
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = "+id)
    )
    # text("SELECT * FROM jobs WHERE id = :val "), val=id
    #the code above is not working, this is why I 
    #choose to only concatenate the sql string + variable 
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
      #return dict(rows[0])
  