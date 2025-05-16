import os
import csv
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import argparse

def predict_folder_images(model_path, images_folder, output_csv):
    # Загружаем модель
    model = tf.keras.models.load_model(model_path)

    # Параметры для обработки изображений
    img_size = (224, 224)

    results = []

    # Проходим по файлам в папке
    for filename in os.listdir(images_folder):
        filepath = os.path.join(images_folder, filename)
        # Проверяем, что это файл и изображение по расширению
        if os.path.isfile(filepath) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Загружаем и обрабатываем изображение
            img = load_img(filepath, target_size=img_size)
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)

            # Предсказание вероятности
            prob = model.predict(x)[0][0]
            pred = 1 if prob > 0.5 else 0

            results.append((filename, pred))

    # Записываем результаты в CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['filename', 'prediction'])
        writer.writerows(results)

    print(f"[INFO] Предсказания сохранены в файл: {output_csv}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Классификация изображений в папке с помощью MobileNetV2")

    # Модель по умолчанию — в папке model внутри докера
    parser.add_argument('--model', type=str, default='model/MobileNetV2_full_model.keras',
                        help="Путь к модели Keras (.keras), по умолчанию model/MobileNetV2_full_model.keras")

    parser.add_argument('--images', type=str, required=True,
                        help="Путь к папке с изображениями")

    parser.add_argument('--output', type=str, default='predictions.csv',
                        help="Путь к выходному CSV файлу")

    args = parser.parse_args()

    if not os.path.exists(args.model):
        print(f"[ERROR] Модель не найдена по пути: {args.model}")
        exit(1)

    if not os.path.exists(args.images) or not os.path.isdir(args.images):
        print(f"[ERROR] Папка с изображениями не найдена или не является директорией: {args.images}")
        exit(1)

    predict_folder_images(args.model, args.images, args.output)
