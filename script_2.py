from sqlalchemy import create_engine
import script

# Establish SQL Server
engine = create_engine('mysql+pymysql://root:815927Ljy!@localhost/teri_baseline')

# Load data to target table
script.df.to_sql('cd8_all', con=engine, index=False, if_exists='append')
