# streamlit_app.py
import streamlit as st
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.schema_manager import SCHEMA_CONTEXT
from src.model_handler import SQLGenerator
from src.database_connector import MedicalDB



# Initialize components
db = MedicalDB()
model = SQLGenerator()

# Configure UI
st.set_page_config(page_title="Medical SQL AI", layout="wide")
st.title("⚕️ Clinical Data Query System")

# Sidebar
with st.sidebar:
    st.header("Database Explorer")
    table = st.selectbox("Preview Table", [
        "patients", "admissions", "prescriptions", "labevents"
    ])
    try:
        st.dataframe(db.execute_safe(f"SELECT * FROM {table} LIMIT 5"))
    except:
        st.error("Couldn't load table preview")

# Main interface
col1, col2 = st.columns([3, 2])

with col1:
    question = st.text_area("Enter Clinical Query:", height=150,
                           placeholder="e.g., List IV antibiotics prescribed in ICU")
    
    if st.button("Generate Query"):
        with st.spinner("Analyzing..."):
            try:
                sql = model.generate_sql(question)
                with st.expander("Generated SQL", expanded=True):
                    st.code(sql, language='sql')
                
                results = db.execute_safe(sql)
                st.dataframe(results, use_container_width=True)
                
            except Exception as e:
                st.error(f"Execution Error: {str(e)}")

with col2:
    st.subheader("Schema Reference")
    st.code(SCHEMA_CONTEXT, language='sql')
    
    st.subheader("Example Queries")
    st.markdown("""
    - "Patients with sepsis and elevated lactate"
    - "Anticoagulants administered via IV"
    - "Blood cultures positive for Staphylococcus"
    - "ICU patients with prolonged mechanical ventilation"
    """)
