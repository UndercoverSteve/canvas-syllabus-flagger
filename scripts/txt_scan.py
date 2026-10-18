#docx import necessary in order to interact with MS Word documents
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from modules.required_elements import required_elements

from docx import Document
from pathlib import Path

EXAMPLES_DIR = Path(__file__).resolve().parent.parent / "example-syllabi"

def check_for_headers(syllabus):
    results = []

    for section, info in required_elements.items():
        if info["typeof"] == "header":
            found_header = False
            for p in syllabus.paragraphs:
                if section.lower() in p.text.lower():
                    results.append(f"{section} found")

                    found_header = True
                    break

            if found_header == False:
                # Didn't find the header
                results.append(f"{section} MISSING")

    return results

def check_for_text(syllabus):
       #Run through code to find text
        #Will print the 'found' message for each instance text is found
        for paragraph in syllabus.paragraphs:
            if text1.lower() in paragraph.text.lower():
                print("Found 'Python' in doc.")
    
        #Search for trext from file
        with open(EXAMPLES_DIR / "cours_desc.txt", "r") as file:
            text2 = file.readlines()
    
        #strip removes extra spaces, newlines, etc.
        #Used for helping compare .txt to .doc
        for term in text2:
            term = term.strip()
    
            #Keep searching if paragraph is not found
            if not term:
                continue
    
            found = False
    
            #Loop to search .doc for text in .txt
            for paragraph in syllabus.paragraphs:
                
                #Make all chars lower case to remove case-sensitive searching
                if term.lower() in paragraph.text.lower():
                    
                    #Return sring 'found' when found to test if this code works
                    results.append(f"Found text")
                    found = True
                    
            #Need an output to provide feedback to user if the text is not found
            if not found:
                results.append(f"Did not find text")

def main_task():
    #Loation of doc to search through
    syllabus = Document(EXAMPLES_DIR / "CS111.docx")

    #stores results to return to main program
    results = check_for_headers(syllabus)

    print(results)

    return results

#TODO:
    #Add additional paragaraphs/syllabus sections to search for
    #Change verbiage from generic paragraph(s) to name of sections; description, AI use, etc.
