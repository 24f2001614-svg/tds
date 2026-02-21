FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir requests pandas fastapi
CMD ["python", "main.py"]
