import json
import logging
from pathlib import Path

# Set up logging
log_file = 'tests/json__Baskakov.log'
logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Path to the directory
directory = Path('ideas_for_test/work_with_json')

# Iterate through all files in the directory
for json_file in directory.glob('*.json'):
    try:
        # Try to open and load the file to check if it is a valid JSON
        with json_file.open('r', encoding='utf-8') as f:
            json.load(f)
        print(f"{json_file.name} is a valid JSON.")
    except (json.JSONDecodeError, IOError) as e:
        # Log an error if the file is not a valid JSON
        logging.error(f"{json_file.name} is not a valid JSON. Error: {str(e)}")
        print(f"{json_file.name} is not a valid JSON. Logged the error.")

print(f"Validation complete. Check {log_file} for errors.")