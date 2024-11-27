import pandas as pd
from tqdm import tqdm
import sqlite3

from apps.config import Config 

#from utils.logger import logger_scraping

class DataManager:
    
    def __init__(self) -> None: 
        self.cf = Config()      
        
    def _get_connection(self):
        
        try:
            conn = sqlite3.connect(f"{self.cf.project_path}/{self.cf.db_name}")
            return conn
        except sqlite3.Error as e:
            print(f'Error connecting to database: {e}') 

            return None


    def initial_create_table(self, table_name="my_table_name"):
        
        with self._get_connection() as conn:        
            try:
                print("DB CHECK")
                query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50),
                        age INT,
                        email VARCHAR(100) UNIQUE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        is_active BOOLEAN DEFAULT TRUE
                    );
                    """
                conn.execute(query)
                conn.commit()

                query = f"""
                    INSERT INTO {table_name} (name, age, email, is_active)
                    VALUES 
                        ('Alice', 30, 'alice@example.com', TRUE),
                        ('Bob', 25, 'bob@example.com', FALSE),
                        ('Charlie', 35, 'charlie@example.com', TRUE),
                        ('David', 28, 'david@example.com', TRUE),
                        ('Eve', 40, 'eve@example.com', FALSE)
                    ON CONFLICT (email) DO NOTHING
                        ;
                    """ 
                conn.execute(query)
                conn.commit()

                        
            except sqlite3.Error as e:
                print(f'Error loading rows from table {table_name}: {e}') 
                conn.rollback()

    def get_all_data_as_df(self, table_name="my_table_name"):
        
        with self._get_connection() as conn:        
            try:
                query = f"SELECT * FROM {table_name}"
            
                return pd.read_sql_query(query, conn)
            
            except sqlite3.Error as e:
                print(f'Error loading rows from table {table_name}: {e}') 
                conn.rollback()