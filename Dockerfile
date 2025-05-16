# Базовый образ Python 3.9 slim
FROM python:3.9-slim

# Обновим pip и установим зависимости
RUN pip install --upgrade pip

# Копируем файл с зависимостями
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем модель в контейнер
COPY model /app/model

# Копируем скрипт
COPY predict_images.py /app/predict_images.py

# Устанавливаем рабочую директорию
WORKDIR /app

# По умолчанию запускаем скрипт, аргументы передаются при запуске контейнера
ENTRYPOINT ["python", "predict_images.py"]
