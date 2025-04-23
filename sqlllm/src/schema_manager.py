import os

def load_schema():
    """Load schema file with absolute path"""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(base_dir, "..", "schema", "medical_schema.sql")
        with open(schema_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error loading schema: {str(e)}")
        return ""

SCHEMA_CONTEXT = f"""
MEDICAL DATABASE SCHEMA

{load_schema()}
"""
