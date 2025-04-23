# Enhancing Reliability of Text-to-SQL Systems through Prompting techniques and Abstention

<p align="center">
  <img src="sqlllm\images\flowchart.png" alt="System Workflow"/>
</p>

The aim is to develop a natural language text-to-SQL generator model specifically for Electronic Health
Records (EHRs), using the MIMIC-IV Demo database gathered from the source
[https://github.com/glee4810/ehrsql-2024]. This will be particularly useful for healthcare professionals
who need to access medical data without deep knowledge of SQL.
The research questions for this project are:
1. Can a text-to-SQL model reliably generate accurate SQL queries from natural language questions
specific to medical contexts (e.g., patient demographics, vital signs, disease survival rates)?
2. How effectively can the model handle unanswerable questions (e.g., asking about weather) or
SQL functionalities that go beyond simple data retrieval.


### Setting up the Environment

```bash
pip install -r requirements.txt
git clone https://github.com/glee4810/ehrsql-2024
```
step 1 : Download and preprocess the database following the instructions in the repository ([link](https://github.com/glee4810/ehrsql-2024?tab=readme-ov-file#database))

step 2 : use the  create_datasets.py file to further preprocess
```bash
python create_datasets.py
```

### Instructions
- Experiment 1: Text-to-SQL Generation (Initial Prompt - Schema of DB, random few shot prompts of Q&A from trainning data) 

Example:
```
streamlit run streamlit_app.py
```

# The solution: 
This solution leverages advanced prompting techniques—particularly in-context learning—to translate natural language questions into executable SQL queries over a structured medical schema. The architecture is designed to modularize key stages of this pipeline, from user interaction to final query execution and result presentation.

Prompting Techniques Utilized:
In-Context Learning: The model is guided using contextual information embedded directly within the prompt.

Few-Shot Prompting: Carefully selected example question-SQL pairs are used to steer the model towards accurate query generation.

Pretrained QA Samples: Representative examples were incorporated during pretraining to enhance the model’s understanding of domain-specific patterns.# DoctorAssist.ai
