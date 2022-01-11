#! python3

""" This imports a word doc and prints out it's contents as plain text"

import docx

def getText(filename):
    doc = docx.Document(filename)
    fulltext = []
    for para in doc.paragraphs:
        fulltext.append(para.text)
    return "\n".join(fulltext)

print(getText("demo.docx"))
