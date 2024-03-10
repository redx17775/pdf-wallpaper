import fitz  # PyMuPDF

input_pdf_path = "Hw1_133747.pdf"
output_pdf_path = "output.pdf"
background_color = (18/255, 18/255, 18/255)

doc = fitz.open(input_pdf_path)
for page in doc:
    page.draw_rect(page.rect, color=None, fill=background_color, overlay=False)

doc.ez_save(output_pdf_path)
doc.close()
print("Background color changed and saved to", output_pdf_path)