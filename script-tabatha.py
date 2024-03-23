from tika import parser

def extract_metadata_tika(file_path):
    parsed = parser.from_file(file_path)
    return parsed["metadata"]

docx_file = "documento.docx"
xlsx_file = "documento.xlsx"
pdf_file = "documento.pdf"


print("Estos son los metadatos de .DOCX:")
print(extract_metadata_tika(docx_file))

print("\nEstos son los metadatos de .XLSX:")
print(extract_metadata_tika(xlsx_file))

print("\nEstos son los metadatos de .PDF:")
print(extract_metadata_tika(pdf_file))