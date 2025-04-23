import dotenv
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os
import pandas as pd
import random
from src.schema_manager import SCHEMA_CONTEXT

class SQLGenerator:
    def __init__(self, train_csv="data/train.csv", n_examples=5):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.examples = self._load_examples(train_csv, n_examples)
    
    def _load_examples(self, csv_path, n):
        """Load n random examples from training split, handling both 'sql' and 'query' columns."""
        try:
            df = pd.read_csv(csv_path)
            df.columns = df.columns.str.strip()
            # Use 'sql' if present, else 'query'
            sql_col = 'sql' if 'sql' in df.columns else 'query'
            # Drop rows with missing data
            df = df.dropna(subset=['question', sql_col])
            n = min(n, len(df))
            return random.sample(list(zip(df['question'], df[sql_col])), n)
        except Exception as e:
            print(f"Example loading error: {str(e)}")
            return []
    
    def generate_sql(self, question):
        prompt = self._build_prompt(question)
        response = self.model.generate_content(prompt)
        return self._clean_sql(response.text)
    
    def _build_prompt(self, question):
        examples = "\n\n".join([f"Q: {q}\nSQL: {sql}" for q, sql in self.examples])
        return f"""
You are a medical SQL expert. Use this schema:
{SCHEMA_CONTEXT}

Examples:
{examples}

Question: {question}
SQL:
"""
    def _clean_sql(self, sql):
    
        """Remove markdown and formatting from SQL response"""
        import re
        # Remove opening code fence and optional 'sql' language tag
        sql = re.sub(r"^```sql\s*", "", sql, flags=re.IGNORECASE)
        # Remove opening code fence without language tag
        sql = re.sub(r"^```\s*", "", sql)
        # Remove closing code fence at the end
        sql = re.sub(r"\s*```\s*$", "", sql)
        # Remove any leading/trailing backticks or whitespace
        sql = sql.strip("` \n")
        # Remove any leading 'sql ' or 'SQL '
        sql = re.sub(r"^\s*sql\s+", "", sql, flags=re.IGNORECASE)
        # Remove inline SQL comments
        sql = re.sub(r"--.*", "", sql)
        # Collapse multiple spaces and remove trailing semicolons
        sql = re.sub(r"\s+", " ", sql).strip().rstrip(';')
        return sql