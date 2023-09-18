import json, requests
import os
import io
import base64
import subprocess
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
    return pytesseract.image_to_string(Image.open('test.png'), lang='eng')
    
@app.errorhandler(404)
def not_found(error):
  resp = jsonify( { 
    u'status': 404, 
    u'message': u'Resource not found' 
  } )
  resp.status_code = 404
  return resp
    
def process_file(path, filename):
    
    # json_data = {path: filename}
    # return json_data
    file_name = path.replace(filename,secure_filename(filename))
    # img3 = cv2.imread(file_name)
    # img3 = np.array(Imageocr)
    gray3 = cv2.cvtColor(Imnp, cv2.COLOR_BGR2GRAY) 

    text3 = pytesseract.image_to_string(gray3, lang='lao', config='--psm 11')
    # target = pytesseract.image_to_string(image, lang='eng', boxes=False, \
        # config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    return text3
