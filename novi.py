import PyPDF2

# Load the PDF file
with open('/Users/ivan/BOT/pks bot docs/wetransfer_bahreinengleski-pdf_2024-01-12_1338/GUIDE FOR ESTABLISHING A COMPANY, JUNE 2023..pdf', 'rb') as f:
    pdf = PyPDF2.PdfReader(f)
    
    # Extract the text from the PDF
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
    
    # Print the extracted text
        print(text)

# poslato na github


# Open a file in write mode
        with open("output.txt", "w") as f:
    # Write the text to the file
           f.write(text)
