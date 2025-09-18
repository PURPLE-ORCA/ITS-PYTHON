from docx import Document
import pandas as pd

doc = Document(r"C:\Users\purple Orca\Documents\EMIG CLASS\ITS-PYTHON\COURSE\SCRIPTS\mywordfile.docx")
data = []

for table in doc.tables:
    for row in table.rows:
        data.append([cell.text for cell in row.cells])

df = pd.DataFrame(data)
df.to_excel('output.xlsx', index=False)
