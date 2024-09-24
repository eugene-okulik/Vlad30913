FROM python:3.9-slim

COPY openweather.py .

COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "openweather.py"]
