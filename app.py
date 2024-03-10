from flask import Flask, render_template, request, send_file
import fitz  # PyMuPDF
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdf_file' not in request.files:
        return "No PDF file uploaded"

    pdf_file = request.files['pdf_file']

    if pdf_file.filename == '':
        return "No selected file"

    # Process the PDF content
    processed_pdf_content = change_background_color(pdf_file)

    # Return the processed PDF content as a downloadable file
    return send_file(
        io.BytesIO(processed_pdf_content),
        download_name='processed_pdf.pdf',
        as_attachment=True
    )

def change_background_color(pdf_file):
    # Create a canvas with a specified background color
    background_color = (18/255, 18/255, 18/255)
    new_pdf = fitz.open()

    # Append the original PDF pages
    original_pdf = fitz.open(stream=pdf_file.read())
    new_pdf.insert_pdf(original_pdf)

    # Iterate through each page and overlay a colored rectangle
    for page_number in range(new_pdf.page_count):
        page = new_pdf[page_number]
        rect = fitz.Rect(0, 0, page.rect.width, page.rect.height)

        # Use draw_rect to fill the entire page with the specified color
        page.draw_rect(rect, color=background_color, fill=background_color, overlay=False)

    new_pdf_stream = io.BytesIO()
    new_pdf.save(new_pdf_stream)

    new_pdf_stream.seek(0)
    return new_pdf_stream.read()

if __name__ == '__main__':
    app.run(debug=True)
