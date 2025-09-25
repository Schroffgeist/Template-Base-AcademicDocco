# Template-Base-AcademicDocco

This repository provides a powerful and flexible template for creating academic papers using R Markdown and LaTeX. It is designed to be used in conjunction with a Large Language Model (LLM) like Gemini to automate the process of turning research notes into a fully formatted, publication-ready document.

## Features

- Based on R Markdown for easy content creation.
- Utilizes LaTeX for high-quality typesetting and formatting.
- Includes a pre-configured bibliography setup with BibTeX.
- Automated processing via the `process_inputs.py` script which calls the Gemini CLI.

## Automated Workflow

1.  **Add Notes**: Place your raw note files (.txt, .md, etc.) into the `input-RawFiles` directory.
2.  **Run the Script**: Execute the automation script from your terminal:
    ```bash
    python process_inputs.py
    ```
3.  **Review Changes**: The script will invoke the Gemini CLI to process your notes, update the bibliography (`Bibliografia.bib`), and populate the R Markdown template (`TemplateDocco-0.Rmd`).
4.  **Compile**: Once the script is finished, you can compile the final PDF using RStudio or by running the following command in an R environment:
    ```R
    rmarkdown::render("TemplateDocco-0.Rmd")
    ```

For more detailed information on the automation, see the `GEMINI.md` file.

## Getting Started

To use this template, you will need the following installed:

- Python 3
- The Gemini CLI (and have it accessible in your system's PATH)
- R and RStudio
- A LaTeX distribution (e.g., MiKTeX, TeX Live)
- The R package `rmarkdown`

## License

This project is licensed under the MIT License.
