import json
import pandas as pd
from pathlib import Path

def build_splits():
    splits = ["train", "valid", "test"]
    for split in splits:
        data = []
        split_dir = Path(f"data/{split}")
        for file in split_dir.glob("*.json"):
            with open(file) as f:
                content = json.load(f)
                # Check if content is a list or has a "data" key
                if isinstance(content, list):
                    data.extend(content)
                elif "data" in content:
                    data.extend(content["data"])
        pd.DataFrame(data).to_csv(f"data/{split}.csv", index=False)

if __name__ == "__main__":
    build_splits()
