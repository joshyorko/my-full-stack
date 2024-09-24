import os
import pandas as pd
import logging
from sqlalchemy import create_engine, MetaData, Table, Column, String, text
from sqlalchemy.orm import sessionmaker
from rich import print

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
POSTGRES_SERVER = os.getenv('POSTGRES_SERVER', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'jaws_db')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'myuser')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'mypassword')

# Define your database URL
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

# Create an engine and a session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

# Read the CSV file in chunks
chunk_size = 5000  # Adjust chunk size as needed
csv_file_path = 'allocation_josh.csv'
df_iterator = pd.read_csv(csv_file_path, chunksize=chunk_size)

# Dynamically create the table definition from the first chunk
first_chunk = next(df_iterator)
def create_table(df, table_name):
    columns = []
    for column_name, dtype in zip(df.columns, df.dtypes):
        columns.append(Column(column_name, String))

    table = Table(table_name, metadata, *columns)
    return table

# Create the table in the database
table_name = 'allocation'
table = create_table(first_chunk, table_name)
metadata.create_all(engine)
logging.info(f'Table {table_name} created successfully.')

# Insert the first chunk into the table
first_chunk.to_sql(table_name, engine, if_exists='append', index=False)
logging.info(f'Inserted first chunk of data into {table_name}.')

# Process the remaining chunks
for chunk in df_iterator:
    chunk.to_sql(table_name, engine, if_exists='append', index=False)
    logging.info(f'Inserted a chunk of data into {table_name}.')

# Query the database to verify the insertion
result = session.execute(text(f'SELECT * FROM {table_name}')).fetchall()
logging.info(f'Fetched {len(result)} rows from {table_name}.')
check = session.execute(text(f'SELECT "CLEARNING HOUSE", COUNT(*) FROM {table_name} GROUP BY "CLEARNING HOUSE"')).fetchall()
print(check)

# Close the session
session.close()
logging.info('Session closed.')