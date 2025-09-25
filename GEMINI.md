# Gemini LLM Instructions for Academic Paper Generation

## 1. Objective

The primary goal is to automate the creation of a well-structured academic paper in PDF format. This process starts with a single text file (`.txt`) provided by a researcher or student, which contains their notes, references, and metadata. This file will be used to populate the R Markdown template (`TemplateDocco-0.Rmd`) and its associated bibliography (`Bibliografia.bib`).

## 2. Project File Structure

- **`GEMINI.md`**: This file. Contains the instructions for the LLM.
- **`TemplateDocco-0.Rmd`**: The main R Markdown template file. The LLM will modify this file extensively.
- **`2025-Headers.tex` & `2025-BeforeBody.tex`**: LaTeX files for custom headers and content. These should generally not be modified unless specifically requested.
- **`sage-plots-for-TemplateDocco-0.tex/Bibliografia.bib`**: The bibliography file. The LLM will add references here.
- **`input.txt`** (Example Name): The user-provided text file containing all the necessary information.

## 3. Workflow Instructions

### Step 1: Receive and Parse the Input File

When the user provides a text file (e.g., `input.txt`), your first task is to read and parse its content. The file should be structured with clear headings to separate different types of information. An ideal format is suggested in Section 4.

You must identify and extract the following components:
- **Personal Info**: Author's name, email, etc.
- **Document Metadata**: Title of the paper, course name, date, abstract.
- **Core Content**: The main body of the research, which may be a collection of disconnected notes, paragraphs, or ideas.
- **References**: A list of citations to be included in the bibliography.

### Step 2: Update the Bibliography

1.  Navigate to `sage-plots-for-TemplateDocco-0.tex/Bibliografia.bib`.
2.  For each reference extracted from the input file, format it correctly as a BibTeX entry.
3.  If the user provides a simple list of references, use your knowledge to find the full BibTeX citation for each source.
4.  Append the new BibTeX entries to the `Bibliografia.bib` file. Ensure there are no duplicate entries.

### Step 3: Parameterize and Update the Rmd File

1.  Open `TemplateDocco-0.Rmd`.
2.  Locate the YAML header at the beginning of the file.
3.  Replace the placeholder values for `title`, `author`, `date`, and other metadata fields with the information extracted from the input file.
4.  If an abstract is provided, ensure it is placed correctly within the Rmd file's structure.

### Step 4: Structure and Enhance the Core Content

This is the most critical step, requiring content generation and structuring.

1.  **Organize the Content**: Take the user's raw notes and ideas and organize them into a standard academic structure. A typical structure includes:
    -   Introduction
    -   Methodology (if applicable)
    -   Main Body / Argument / Results
    -   Discussion
    -   Conclusion

2.  **Write Missing Sections**: If the user's notes lack an introduction or conclusion, you must write them.
    -   The **Introduction** should introduce the topic, state the paper's purpose, and briefly outline the structure.
    -   The **Conclusion** should summarize the main points and provide final thoughts or suggestions for future research.

3.  **Ensure Coherence and Flow**: The user's ideas may be disjointed. Your task is to connect them smoothly.
    -   Write transition sentences and paragraphs to link different ideas.
    -   Rephrase sentences to improve clarity and adopt a formal, academic tone.
    -   Ensure a logical progression of the argument from one section to the next.

4.  **Integrate Citations**: As you structure the content, insert LaTeX-style citations (e.g., `[@key]`) where appropriate, linking back to the entries you added to the `.bib` file.

### Step 5: Compile the Final PDF

1.  Once the `.Rmd` and `.bib` files are fully updated, execute the command to render the document. The standard command is:
    ```R
    rmarkdown::render("TemplateDocco-0.Rmd")
    ```
2.  This will generate the final `TemplateDocco-0.pdf`.

### Step 6: Present the Final Output

Inform the user that the process is complete and that the final paper is available in the `TemplateDocco-0.pdf` file.

## 4. Example `input.txt` Structure

To make parsing reliable, the user should be encouraged to format their input file as follows:

```
---
PersonalInfo:
  Author: Jane Doe
  Email: jane.doe@email.com

DocumentInfo:
  Title: The Impact of Climate Change on Marine Ecosystems
  Course: BIO-301 Advanced Ecology
  Date: 2025-09-24
  Abstract: This paper explores the multifaceted impacts of rising global temperatures on the biodiversity and stability of marine ecosystems, focusing on coral bleaching and species migration.

---
CoreContent:

# Introduction Idea
Start with a hook about the planet warming. Mention the ocean as a critical carbon sink.

# Main Point 1
Coral bleaching is a major issue. High temperatures cause corals to expel algae. Talk about the Great Barrier Reef. Maybe find a stat on this.

# Main Point 2
Fish populations are moving towards the poles to find cooler water. This disrupts fisheries and local economies. Mention the North Atlantic cod migration.

# Conclusion Idea
Summarize the two main points. End with a call to action for international cooperation on climate policy.

---
References:

1.  "The Uninhabitable Earth" by David Wallace-Wells
2.  IPCC, 2021: Climate Change 2021: The Physical Science Basis.
3.  A paper by Pauly and Zeller on fishery data.

---
```
