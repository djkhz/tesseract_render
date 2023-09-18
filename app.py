from flask import Flask
from PIL import Image
import pytesseract

app = Flask(__name__)


@app.route('/')

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/ocr', methods=['GET','POST'])
def ocr():
    # test.png from the pytesseract project: https://github.com/madmaze/pytesseract/tree/master/tests/data
    #return pytesseract.get_tesseract_version()
    return pytesseract.image_to_string(Image.open('test.png'), lang='lao')
