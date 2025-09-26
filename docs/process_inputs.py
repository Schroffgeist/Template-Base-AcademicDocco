import os
import subprocess
import sys

# --- Configuration ---
INPUT_DIR = "../input-RawFiles"
PROMPT_FILE = "prompt.txt"
GEMINI_MODEL = "gemini-2.5-pro" 

# --- 1. Check for input directory ---
if not os.path.isdir(INPUT_DIR):
    print(f"Error: Input directory '{INPUT_DIR}' not found.")
    print("Please create it and add your raw text files.")
    sys.exit(1)

# --- 2. Find files to process ---
try:
    file_paths = [os.path.join(f"@'{os.path.abspath(INPUT_DIR)}", f"{f}'") for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]
except OSError as e:
    print(f"Error reading directory {INPUT_DIR}: {e}")
    sys.exit(1)

if not file_paths:
    print(f"Warning: No files found in '{INPUT_DIR}'. Nothing to process.")
    sys.exit(0)

print(f"Found {len(file_paths)} file(s) to process:")
for path in file_paths:
    print(f"- {path}")

# --- 3. Read the base prompt ---
try:
    with open(PROMPT_FILE, 'r') as f:
        base_prompt = f.read()
except FileNotFoundError:
    print(f"Error: The prompt file '{PROMPT_FILE}' was not found.")
    sys.exit(1)

# --- 4. Construct the final prompt ---
files_string = "\n".join(file_paths)
final_prompt = f"{base_prompt}\n{files_string}"

# --- 5. Build and execute the Gemini CLI command ---
command = [
    "gemini",
    "-p",
    "-y",
    final_prompt,
    "-m",
    GEMINI_MODEL
]

print("\n--- Executing Gemini CLI ---")
try:
    # Using subprocess.run to execute the command
    result = subprocess.run(command, capture_output=True, text=True, check=True) 
    
    print("--- Gemini CLI Finished Successfully ---")
    print("Stdout:")
    print(result.stdout)
    if result.stderr:
        print("Stderr:")
        print(result.stderr)

except FileNotFoundError:
    print("Error: 'gemini' command not found.")
    print("Please ensure the Gemini CLI is installed and in your system's PATH.")
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print("--- Gemini CLI Failed ---")
    print(f"Return Code: {e.returncode}")
    print("Stdout:")
    print(e.stdout)
    print("Stderr:")
    print(e.stderr)
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
