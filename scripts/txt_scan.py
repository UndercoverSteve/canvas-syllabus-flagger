#docx import necessary in order to interact with MS Word documents
from docx import Document

def main_task():
    #Loation of doc to search through
    syllabus = Document(r"C:\Users\curti\OneDrive\Documents\CS111.docx")

    #stores results to return to main program
    results = []

    #Search for individual words
    text1 = "Python"

    #Run through code to find text
    #Will print the 'found' message for each instance text is found
    for paragraph in syllabus.paragraphs:
        if text1.lower() in paragraph.text.lower():
            print("Found 'Python' in doc.")

    #Search for trext from file
    with open("cours_desc.txt", "r") as file:
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

        return results

#TODO:
    #Add additional paragaraphs/syllabus sections to search for
    #Change verbiage from generic paragraph(s) to name of sections; description, AI use, etc.
