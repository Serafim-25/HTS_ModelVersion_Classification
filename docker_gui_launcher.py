import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import threading

DOCKER_IMAGE_NAME = "hts_modelversion_classifier"
DOCKER_TAR_PATH = "hts_modelversion_classifier.tar"


def run_docker(image_path, output_path, progress, btn):
    try:
        btn.config(state="disabled")
        progress.start(10)  # Запускаем анимацию прогресс-бара

        messagebox.showinfo("Загрузка", "Загружается Docker-образ...")
        subprocess.run(["docker", "load", "-i", DOCKER_TAR_PATH], check=True)

        messagebox.showinfo("Запуск", "Запускается классификация...")
        subprocess.run([
            "docker", "run", "--rm",
            "-v", f"{image_path}:/app/images",
            "-v", f"{output_path}:/app/output",
            DOCKER_IMAGE_NAME,
            "--images", "/app/images",
            "--output", "/app/output/predictions.csv"
        ], check=True)

        messagebox.showinfo("Готово", f"Файл 'predictions.csv' сохранён в: {output_path}")

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при работе с Docker:\n{e}")
    finally:
        progress.stop()  # Останавливаем прогресс-бар
        btn.config(state="normal")
        # Удаляем образ и сообщаем
        subprocess.run(["docker", "rmi", DOCKER_IMAGE_NAME], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        messagebox.showinfo("Удаление", f"Docker-образ '{DOCKER_IMAGE_NAME}' удалён")


def select_and_run(progress, btn):
    image_path = filedialog.askdirectory(title="Выберите папку с изображениями для классификации")
    if not image_path:
        return
    output_path = filedialog.askdirectory(title="Выберите папку для сохранения CSV с предсказаниями")
    if not output_path:
        return

    # Запускаем в отдельном потоке, чтобы UI не зависал
    threading.Thread(target=run_docker, args=(image_path, output_path, progress, btn), daemon=True).start()

if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, '1.ico')  # путь во временной папке PyInstaller
else:
    icon_path = os.path.abspath('icon/1.ico')        # путь при обычном запуске .py

# Интерфейс
window = tk.Tk()
window.title("Классификатор диаграмм ВТСП")
window.iconbitmap(default=icon_path)
window.resizable(False, False)

label = tk.Label(
    window,
    text="Запустите классификацию и выберите папку с изображениями для классификации и папку для сохранения CSV с предсказаниями",
    font=("Segoe UI", 12),
    wraplength=380,
    justify="center"
)

label.pack(pady=10, padx=10)

progress = ttk.Progressbar(window, mode="indeterminate")
progress.pack(pady=10, fill='x', padx=20)

start_btn = tk.Button(window, text="Запустить", font=("Segoe UI", 11),
                      command=lambda: select_and_run(progress, start_btn))
start_btn.pack(pady=10)

footer = tk.Label(
    window,
    text="Docker Desktop должен быть установлен и запущен\nФайлы docker_gui_launcher.exe и hts_modelversion_classifier.tar должны быть расположены в одной папке",
    font=("Segoe UI", 9),
    fg="gray",
    wraplength = 380,
    justify = "center"
)

footer.pack(side="bottom", pady=10, padx=10)

window.mainloop()
