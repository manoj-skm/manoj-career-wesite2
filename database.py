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

