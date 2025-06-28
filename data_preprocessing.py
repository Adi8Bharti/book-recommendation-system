import pandas as pd
import sqlite3

def load_data(file_path):
    """Load and clean book ratings data."""
    data = pd.read_csv(file_path)
    data.fillna(0, inplace=True)
    return data

def setup_database(data, db_name='books.db'):
    """Store data in SQLite database."""
    conn = sqlite3.connect(db_name)
    data.to_sql('ratings', conn, if_exists='replace', index=False)
    conn.close()
    return conn