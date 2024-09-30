import pytesseract
from PIL import Image
import gradio as gr
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# OCR processing function
def process_image(image, keyword=None):
    extracted_text = pytesseract.image_to_string(image)
    if keyword:
        # Highlight keyword matches
        highlighted_text = extracted_text.replace(keyword, f"**{keyword}**")
        return highlighted_text
    return extracted_text

# Gradio web interface
iface = gr.Interface(
    fn=process_image, 
    inputs=[gr.Image(type="pil"), gr.Textbox(label="Keyword (Optional)")], 
    outputs="text", 
    title="OCR and Document Search",
    description="Upload an image and search for keywords in the extracted text."
)

# Launch the app
iface.launch()
