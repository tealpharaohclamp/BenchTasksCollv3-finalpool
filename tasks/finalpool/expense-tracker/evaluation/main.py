"""Evaluation script for expense-tracker task."""

import os
import json


def evaluate():
    """Evaluate if the expense tracking solution is correct."""
    # Check if the workspace has the expected files
    required_files = ["expenses.json", "categories.json"]
    
    results = {}
    for file in required_files:
        results[file] = os.path.exists(file)
    
    all_passed = all(results.values())
    
    return {
        "passed": all_passed,
        "results": results
    }


if __name__ == "__main__":
    result = evaluate()
    print(json.dumps(result, indent=2))
