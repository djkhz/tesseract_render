#import json, requests
#import os
#import io
#import base64
#import subprocess
#from flask import Flask
#from PIL import Image
#import pytesseract
#import cv2
#import regex as rx
#import numpy as np
#import pandas as pd
#import array

import json, requests
import os
import io
import base64
import subprocess
import sys
import logging
import shutil
from flask import Flask, jsonify, request, redirect, url_for, render_template, send_from_directory,flash,current_app
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
import flask_sijax
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import regex as rx
import numpy as np
import pandas as pd
import array
from laonlp.tokenize import word_tokenize as ltoken
from nltk import word_tokenize
import pyreadr
import re
import urllib.request
import string


#app = Flask(__name__)
app = Flask(__name__, static_url_path="/static")
#app.logger.addHandler(logging.StreamHandler(sys.stdout))
#app.logger.setLevel(logging.ERROR)
mode = 'RGB' # for color image “L” (luminance) for greyscale images, “RGB” for true color images, and “CMYK” for pre-press images.
size = (640, 480)
color = (73, 109, 137)
Imageocr = Image.new(mode, size, color)
Imnp =np.array([])
# app.some_model = pd.read_excel("/app/data/sila_data.xlsx", sheet_name="Book lala", keep_default_na= False, na_values=[""])
#pytesseract.pytesseract.tesseract_cmd = '/app/usr/bin/tesseract'


@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/ocr', methods=['GET','POST'])
def ocr():
    # test.png from the pytesseract project: https://github.com/madmaze/pytesseract/tree/master/tests/data
    #return pytesseract.get_tesseract_version()
    return pytesseract.image_to_string(Image.open('test.png'), lang='eng')
    
@app.route('/ocx', methods=['GET','POST'])
def ocx():
    # test.png from the pytesseract project: https://github.com/madmaze/pytesseract/tree/master/tests/data
    #return pytesseract.get_tesseract_version()
    pytesseract.pytesseract.tesseract_cmd = '/app/.usr/bin/tesseract'
    return pytesseract.image_to_string(Image.open('test.png'), lang='eng')

@app.route('/ocy', methods=['GET','POST'])
def ocxy():
    # test.png from the pytesseract project: https://github.com/madmaze/pytesseract/tree/master/tests/data
    #return pytesseract.get_tesseract_version()
    pytesseract.pytesseract.tesseract_cmd = '/app/usr/bin/tesseract'
    return pytesseract.image_to_string(Image.open('test.png'), lang='eng')

@app.route('/ocz', methods=['GET','POST'])
def ocxz():
    # test.png from the pytesseract project: https://github.com/madmaze/pytesseract/tree/master/tests/data
    #return pytesseract.get_tesseract_version()
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
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
