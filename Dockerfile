FROM python:3.8.5-buster

RUN pip install --upgrade pip

EXPOSE 4000

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

CMD ["python", "src/app.py"]