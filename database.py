from sqlalchemy import create_engine,text

DATABASE_URL = "mysql+pymysql://root:wpXaRAJzfQymZXPXBWsjPjrrSERqbxaW@monorail.proxy.rlwy.net:51952/railway"
engine = create_engine(DATABASE_URL)
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM  jobs;"))  # Fetch all tables in the database

    jobs = []
    for row in result.mappings():
        jobs.append(dict(row))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id};"))
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])