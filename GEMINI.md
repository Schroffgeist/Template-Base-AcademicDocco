# Gemini LLM Instructions for Academic Paper Generation

## 1. Objective

The primary goal is to automate the creation of a well-structured academic paper in PDF format. This process is driven by a Python script that orchestrates the analysis and modification of the document by a headless Gemini instance.

## 2. Project File Structure

- **`GEMINI.md`**: This file. Contains the high-level instructions for the LLM.
- **`docs/process_inputs.py`**: The main Python script that automates the entire workflow.
- **`docs/prompt.txt`**: A template file containing the detailed instructions for the headless Gemini instance.
- **`docs/input-RawFiles/`**: A directory where the user places all their raw notes, data, and reference files.
- **`docs/template.Rmd`**: The main R Markdown template file that will be modified.
- **`docs/assets/Bibliografia.bib`**: The bibliography file that will be updated.

## 3. Automated Workflow

This project uses an automated script, `process_inputs.py`, to manage the paper generation process. The script performs the following actions:

1.  **Scans for Inputs**: It searches the `docs/input-RawFiles` directory for all user-provided files.
2.  **Constructs Prompt**: It reads the instructions from `prompt.txt` and appends the list of found file paths to it.
3.  **Executes Gemini CLI**: It calls the Gemini CLI in headless mode (`gemini -p -y ...`), feeding it the constructed prompt. This instructs Gemini to perform the core content generation and file editing tasks.

### Gemini's Role (Headless Operation)

When executed by the script, the headless Gemini instance will perform the following based on the instructions in `prompt.txt`:

1.  **Parse All Inputs**: Read and analyze the content from all the file paths provided in the prompt.
2.  **Extract & Update Bibliography**: Identify references and append them as correctly formatted BibTeX entries to `docs/assets/Bibliografia.bib`.
3.  **Extract & Update Rmd**: Identify personal info, document metadata, and the core content. Use this to replace the placeholder values in the YAML header and body of `docs/template.Rmd`.
4.  **Structure and Enhance Content**: This is the most critical step. The LLM will:
    -   Organize the raw notes into a standard academic structure (Introduction, Main Body, Conclusion, etc.).
    -   Write missing sections (like the introduction or conclusion) if they are not present in the notes.
    -   Ensure a coherent flow by writing transition sentences and rephrasing content for clarity and an academic tone.
    -   Integrate LaTeX-style citations (`[@key]`) throughout the text, linking to the entries in the `.bib` file.

### Final Step: Manual Compilation

After the script and the headless Gemini instance have finished, the user must manually compile the final PDF using their R environment:

```R
rmarkdown::render("docs/template.Rmd")
```
```
