FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

RUN useradd -m appuser
USER appuser

CMD ["python", "app.py"]