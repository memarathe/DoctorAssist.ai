# # database_connector.py
# import sqlite3
# import pandas as pd
# import streamlit as st

# class MedicalDB:
#     def __init__(self, db_path="mimic_iv.sqlite"):
#         self.db_path = db_path
    
#     @st.cache_resource
#     def get_connection(_self):
#         return sqlite3.connect(_self.db_path)
    
#     def execute_safe(_self, sql, limit=100):
#         """Execute query with safety limits"""
#         conn = _self.get_connection()
#         try:
#             if "LIMIT" not in sql.upper():
#                 sql += f" LIMIT {limit}"
#             return pd.read_sql(sql, conn)
#         except Exception as e:
#             raise ValueError(f"SQL Error: {str(e)}")
    
#     def validate_sql(_self, generated_sql, expected_sql):
#         """Compare generated vs expected SQL"""
#         try:
#             gen_result = _self.execute_safe(generated_sql)
#             exp_result = _self.execute_safe(expected_sql)
#             return gen_result.equals(exp_result)
#         except:
#             return False


import sqlite3
import pandas as pd
import streamlit as st

@st.cache_resource
def get_connection(db_path="mimic_iv.sqlite"):
    """Create a new connection per Streamlit session."""
    return sqlite3.connect(
        db_path,
        check_same_thread=False,
        timeout=10
    )

class MedicalDB:
    def __init__(self, db_path="./mimic_iv.sqlite"):
        self.db_path = db_path

    def execute_safe(self, sql, limit=100):
        """Execute query with thread-safe connection handling."""
        conn = get_connection(self.db_path)
        try:
            if "LIMIT" not in sql.upper():
                sql += f" LIMIT {limit}"
            return pd.read_sql_query(sql, conn)
        except sqlite3.Error as e:
            raise ValueError(f"SQL Error: {str(e)}")

    def get_table_sample(self, table_name):
        """Preview a table."""
        conn = get_connection(self.db_path)
        return pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5", conn)


