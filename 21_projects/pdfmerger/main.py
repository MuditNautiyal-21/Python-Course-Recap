# Lets create a simple python script that uses PyPDF2.

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("Mudit_Nautiyal_Buildots_Cover_Letter.pdf")

reader2 = PdfReader("resume1.pdf")

number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)

number_of_pages2 = len(reader2.pages)
print(number_of_pages2)

text2 = reader2.pages[number_of_pages2-1].extract_text()

print("\nNew Text ---------------->\n")

print(text2)

# Lets now merge text 1 and text 2 into a new PDF file and save it.

writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)
for page in reader2.pages:
    writer.add_page(page)

with open("merged_output.pdf", "wb") as output_pdf:
    writer.write(output_pdf)
print("\nMerged PDF created successfully as 'merged_output.pdf'.")
# This script reads two PDF files, extracts text from them, and merges the pages into a new PDF file.
# Make sure to have PyPDF2 installed in your Python environment.

# Lets try merging the two PDFs directly without extracting text.

writer2 = PdfWriter()

for page in reader.pages:
    writer2.add_page(page)
for page in reader2.pages:
    writer2.add_page(page)

with open("directly_merged_output.pdf", "wb") as output_pdf2:
    writer2.write(output_pdf2)

print("\nDirectly Merged PDF created successfully as 'directly_merged_output.pdf'.")
# This script merges the two PDF files directly without extracting text and saves it as a new PDF file.

# There is another way:

pdfs = []
merger = PdfWriter()

n = int(input("Enter the number of PDFs you want to merge: "))

for i in range(n):
    name = input(f"Enter the name of PDF {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

output_file_name = input("Please enter the name you would want to name your merged PDF: ")

merger.write(output_file_name)
merger.close()