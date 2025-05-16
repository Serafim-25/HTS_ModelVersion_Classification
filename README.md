# Инструкция по установке и запуску

1. Скачайте и установите **Docker Desktop**  
   [Docker Desktop](https://www.docker.com/products/docker-desktop) — выберите версию для Windows и установите.

2. Перезагрузите компьютер.

3. Запустите **Docker Desktop**.  
   При первом запуске может появиться запрос на установку подсистемы Linux для Windows (WSL). Подтвердите установку.

4. Перезагрузите компьютер после установки подсистемы.

5. Снова откройте **Docker Desktop**.

6. Создайте аккаунт Docker (если его ещё нет) и войдите в систему.

---

# Скачайте оба файла:

[![Скачать docker_gui_launcher.exe](https://img.shields.io/badge/Скачать-docker_gui_launcher.exe-blue)](https://github.com/Serafim-25/HTS_ModelVersion_Classification/raw/main/hts_modelversion_classifier/docker_gui_launcher.exe)  
[![Скачать hts_modelversion_classifier.tar](https://img.shields.io/badge/Скачать-hts_modelversion_classifier.tar-blue)](https://github.com/Serafim-25/HTS_ModelVersion_Classification/raw/main/hts_modelversion_classifier/hts_modelversion_classifier.tar)

---

# Запуск программы

1. Скачанные файлы поместите в одну папку

3. Запустите `docker_gui_launcher.exe`

4. В открывшемся окне:

   - Выберите папку с изображениями для классификации.  
   - Выберите папку для сохранения CSV-файла с результатами.

5. Дождитесь завершения работы программы.

6. После завершения закройте окно приложения.

P.S. На всем пути работы программы Вас будут сопровождать уведомления о завершенных процессах и прогресс-бар. Некоторые процессы могут идти долго - ждите) В основном это касается процесса загрузки docker-образа, который происходит в самом начале - после выбора всех необходимых папок из шага 4.
