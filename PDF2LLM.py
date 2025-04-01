import os
import PyPDF2
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


###ChromeRider
###ProphetDiceBot

# Download NLTK stopwords if not already present
nltk.download('stopwords')
nltk.download('punkt')

def extract_text_from_pdfs(pdf_files):
    text_data = ""
    for pdf_file in pdf_files:
        with open(pdf_file, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text_data += page.extract_text() + " "
    return text_data

def condense_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    filtered_text = [word.lower() for word in words if word.lower() not in stop_words and word.isalpha()]
    return " ".join(filtered_text)

def main(pdf_folder):
    pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    extracted_text = extract_text_from_pdfs(pdf_files)
    condensed_text = condense_text(extracted_text)
    print("Condensed Text:")
    print(condensed_text)
    with open("content.txt", "a") as f:
        f.write(f'\n{condensed_text} \n')
    print("complete")



# Example usage
if __name__ == "__main__":
    pdf_folder_path = "./pdfs"  # Change this to your PDF folder path
    main(pdf_folder_path)
