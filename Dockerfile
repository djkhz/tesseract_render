FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get -qq -y install tesseract-ocr && \
    apt-get -qq -y install tesseract-ocr-lao && \
    apt-get -qq -y install libtesseract-dev && \
    apt-get -qq -y libleptonica-dev
#    apt-get -qq -y libsm6 && \
#    apt-get -qq -y libxrender1 && \
#    apt-get -qq -y libfontconfig1 && \
#    apt-get -qq -y libice6 

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app"]
