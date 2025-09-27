# Gemini Agent for Academic Paper Generation

This project utilizes a headless Gemini instance to automate the generation of academic papers from raw notes and templates.

## Role of the Gemini Agent

The Gemini agent, when invoked by the `process_inputs.py` script, performs the following key tasks:

1.  **Input Analysis**: Reads and analyzes content from user-provided raw note files (`input-RawFiles/`).
2.  **Metadata Extraction**: Identifies and extracts personal information, document metadata, core content, and references from the input files.
3.  **Bibliography Management**: Updates the `sage-plots-for-template.tex/Bibliografia.bib` file with correctly formatted BibTeX entries based on extracted references.
4.  **Template Population**: Populates the YAML header and body of `template.Rmd` with extracted metadata and core content.
5.  **Content Structuring and Enhancement**: Organizes raw notes into a standard academic structure (Introduction, Main Body, Conclusion, etc.), writes missing sections, ensures coherent flow, and integrates LaTeX-style citations.

## Workflow Integration

The Gemini agent is an integral part of the automated workflow:

-   The `process_inputs.py` script constructs a detailed prompt for the Gemini CLI, including paths to all input files.
-   The Gemini CLI is executed in headless mode, processing the prompt and performing the content generation and file editing tasks.
-   The output of the Gemini agent (modified `template.Rmd` and `Bibliografia.bib`) is then used by the user to manually compile the final PDF using R Markdown.

For more details on the overall workflow, refer to the `README.md` and `docs/GEMINI.md` files.