FROM python:3.10

WORKDIR /app

ENV PYTHONPATH=/app

COPY app/ /app/
COPY tests/ /app/tests/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]