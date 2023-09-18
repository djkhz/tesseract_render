FROM python:3.9.6

RUN apt-get update && \
    apt-get -qq -y install tesseract-ocr && \
    apt-get -qq -y install tesseract-ocr-lao && \
    apt-get -qq -y install libtesseract-dev  && \
    apt-get -qq -y install libleptonica-dev && \
    apt-get -qq -y install libsm6 && \
    apt-get -qq -y install libxrender1 && \
    apt-get -qq -y install libfontconfig1 && \
    apt-get -qq -y install libice6 

WORKDIR /app
#RUN dpkg -L tesseract-ocr
#RUN dpkg -L tesseract-ocr-lao

RUN ls /app/.usr/bin
# OR See everything (in a windows container)...

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

#RUN python3 -m nltk.downloader punkt
RUN [ "python3", "-c", "import nltk; nltk.download('punkt', download_dir='/usr/local/nltk_data')" ]

COPY . .

CMD ["gunicorn", "app:app"]
