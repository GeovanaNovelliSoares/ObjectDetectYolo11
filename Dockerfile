FROM python:3

COPY . /app

WORKDIR /app

CMD ["python", "python contarObjetos.py"]