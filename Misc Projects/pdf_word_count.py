import PyPDF2
  
# Creates a pdf file object
pdfFileObj = open(r"macbeth_PDF_FolgerShakespeare.pdf", "rb")
  
# Creates a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
  
# Prints number of pages in pdf file
print(len(pdfReader.pages))
  
# Creates a page object
pageObj = pdfReader.pages[25]
  
# Extracts text from page
words = pageObj.extract_text().split()
# Prevents program from counting words not wanted
disallowed_words = ["FTLN"]
# Keeps count of every word from the pdf
word_count = {} 
for word in words:
    if word in word_count and word not in disallowed_words:
        word_count[word] += 1
    else:
        word_count[word] = 1 
        
for word in sorted(word_count, key=word_count.get, reverse=True)[:200]:
    print(f'{word}: {word_count[word]}')


