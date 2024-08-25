FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENV DB_NAME="" DB_USER="" DB_PASSWORD="" DB_PORT=0 DB_HOST=""

CMD ["python", "main.py"]
