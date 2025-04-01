# PDF2LLM


#Overview

This script extracts text from multiple PDF files, condenses it by removing stopwords and non-essential words, and returns a concise summary while preserving key information. It can be used to preprocess documents before passing them to a language model (LLM) for analysis.

#Features

Loads multiple PDFs from a specified directory

Extracts text from all pages

Removes stopwords and non-essential words

Outputs a condensed version of the extracted text


#Requirements

Ensure you have the following dependencies installed before running the script:

pip install PyPDF2 nltk

Additionally, download the necessary NLTK resources:

import nltk
nltk.download('stopwords')
nltk.download('punkt')

#Usage

1. Place all PDF files inside a folder (e.g., pdfs/).


2. Update the pdf_folder_path variable in main() with your folder path.


3. Run the script:



python script.py

4. The condensed text will be printed in the console.



#Example

Input (original text from a PDF):

"Here is my text. It has my information inside. The text is short."

Output (after condensation):

"text information short"

Using with an LLM

To pass the processed text to an LLM:

1. Store the output in a file or database.


2. Feed the condensed text as input to the LLM for further analysis.


3. Use the processed text for summarization, classification, or retrieval tasks.



#Customization

Modify the stopwords list to retain domain-specific terms.

Implement additional NLP techniques like named entity recognition (NER) to refine the output.


#Notes

This script is optimized for text-heavy PDFs. Scanned documents may require OCR preprocessing.

Ensure PDFs are structured properly to maximize extraction accuracy.


#License

This script is open-source and available for modification and distribution.


