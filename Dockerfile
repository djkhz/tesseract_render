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

COPY requirements.txt requirements.txt
CMD python
CMD import nltk
CMD nltk.download()

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app"]
