# importing Flask and other modules
from flask import Flask, request, render_template 
from spire.pdf.common import *
from spire.pdf import *


# Flask constructor
app = Flask(__name__) 

# Create a PdfDocument object
doc = PdfDocument()

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
	if request.method == "POST":
            myFile = request.form.get("filename")
            # Load a PDF file
            doc.LoadFromFile(myFile)
            # Loop through the pages in the document
            for i in range(doc.Pages.Count):
    
                # Get a particular page
                page = doc.Pages[i]

                # Set background color 
                page.BackgroundColor = Color.get_MediumPurple
                
        # Save the document to a different file
        doc.SaveToFile("output/%s_NewWallpaper.pdf",myFile)

if __name__=='__main__':
    app.run()
