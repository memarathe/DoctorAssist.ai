import os
import json

def load_split(split_dir: str):
    """Load questions and SQL from a split directory"""
    data = []
    for filename in os.listdir(split_dir):
        if filename.endswith(".json"):
            with open(os.path.join(split_dir, filename)) as f:
                data.extend(json.load(f)["data"])
    return data

# Example usage:
TRAIN_DATA = load_split("data/train")
VAL_DATA = load_split("data/valid") 
TEST_DATA = load_split("data/test")
