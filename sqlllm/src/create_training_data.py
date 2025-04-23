# create_training_data.py
import json
import pandas as pd

def build_dataset():
    with open('data/data.json') as f:
        questions = json.load(f)['data']
    with open('data/answer.json') as f:
        answers = json.load(f)
    with open('data/annotated.json') as f:
        annotated = json.load(f)

    training_data = []
    for q in questions:
        qid = q['id']
        training_data.append({
            'question': q['question'],
            'sql': annotated.get(qid, {}).get('query'),
            'answer': str(answers.get(qid))
        })
    
    pd.DataFrame(training_data).to_csv('medical_train.csv', index=False)

if __name__ == "__main__":
    build_dataset()
    print("Training data built successfully.")