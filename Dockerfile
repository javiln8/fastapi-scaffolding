FROM python:3.9-slim

WORKDIR /app

ENV PYTHONPATH=/app

ADD . /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
