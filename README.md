# Academic Paper Template

This repository provides a powerful and flexible template for creating academic papers using R Markdown and LaTeX. It is designed to be used in conjunction with a Large Language Model (LLM) like Gemini to automate the process of turning research notes into a fully formatted, publication-ready document.

## How to Use This Template

1.  Click the "**Use this template**" button on the GitHub repository page to create a new repository based on this template.
2.  Clone your newly created repository to your local machine.

## Directory Structure

-   `docs/`: Contains the core template and automation files.
    -   `template.Rmd`: The main R Markdown template file.
    -   `assets/`: Contains all the assets for the document, such as bibliography files, plots, and logos.
    -   `process_inputs.py`: The Python script that automates the workflow.
    -   `prompt.txt`: The prompt for the Gemini CLI.
-   `input-RawFiles/`: Place your raw note files (.txt, .md, etc.) in this directory.

## Automated Workflow

1.  **Add Notes**: Place your raw note files (.txt, .md, etc.) into the `input-RawFiles` directory.
2.  **Run the Script**: Execute the automation script from your terminal:
    ```bash
    python docs/process_inputs.py
    ```
3.  **Review Changes**: The script will invoke the Gemini CLI to process your notes, update the bibliography (`docs/assets/Bibliografia.bib`), and populate the R Markdown template (`docs/template.Rmd`).
4.  **Compile**: Once the script is finished, you can compile the final PDF using RStudio or by running the following command in an R environment:
    ```R
    rmarkdown::render("docs/template.Rmd")
    ```

For more detailed information on the automation, see the `GEMINI.md` file.

## Getting Started

To use this template, you will need the following installed:

-   Python 3
-   The Gemini CLI (and have it accessible in your system's PATH)
-   R and RStudio
-   A LaTeX distribution (e.g., MiKTeX, TeX Live)
-   The R package `rmarkdown`

## License

This project is licensed under the MIT License.