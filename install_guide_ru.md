0. Видео инструкция по установке: https://youtu.be/qxz_vm806j0

1. (ДОПОЛНИТЕЛЬНО ДЛЯ ЧИСТОЙ УСТАНОВКИ) Удалите все установленные версии Python и Cuda, затем перезагрузите компьютер.

2. Загрузите и установите Python версии 3.11.6. На начальном экране установщика активируйте опцию "Add Python 3.11.6 to PATH"! [скачать](https://www.python.org/downloads/)
![](https://github.com/SunOner/yolov8_aimbot/blob/main/media/python.png)

3. Загрузите и распакуйте файлы aimbot Yolov8 [скачать](https://github.com/SunOner/yolov8_aimbot)
![](https://github.com/SunOner/yolov8_aimbot/blob/main/media/aimbot.png)

4. Загрузите и установите Cuda версии 12.1, затем перезагрузите компьютер [скачать](https://developer.nvidia.com/cuda-12-1-0-download-archive)
![](https://github.com/SunOner/yolov8_aimbot/blob/main/media/cuda.png)

5. Откройте командную строку и введите `python -m pip install --upgrade pip`, затем введите `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`

6. Загрузите [TensorRT](https://disk.yandex.ru/d/mgiPzH8fCL83qw) и распакуйте файлы в папку yolov8_aimbot-main.

7. Откройте командную строку и введите `cd C:/путь_где_вы_распаковали/yolov8_aimbot-main/TensorRT-8.6.1.6/python`, затем введите `pip install tensorrt-8.6.1-cp311-none-win_amd64.whl`

8. Нажмите WIN + R и введите `sysdm.cpl`.
- Нажмите на "Дополнительно" (Advanced), затем "Переменные среды" (Environment variables)...
![](https://github.com/SunOner/yolov8_aimbot/blob/main/media/environment_variables.png)
- Дважды щелкните по `path`.
![](https://github.com/SunOner/yolov8_aimbot/blob/main/media/environment_variables_path.png)
- Нажмите `Новая` (New) и введите `C:/путь_где_вы_распаковали/yolov8_aimbot-main/TensorRT-8.6.1.6/lib`
- (ДОПОЛНИТЕЛЬНО) Перезагрузите компьютер.

9. Скопируйте все файлы из `C:/путь_где_вы_распаковали/yolov8_aimbot-main/TensorRT-8.6.1.6/lib` и вставьте в `C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v12.1/bin`

10. Откройте командную строку и введите `cd C:/путь_где_вы_распаковали/yolov8_aimbot-main/`, затем введите `pip install -r requirements.txt`

11. Попробуйте запустить aimbot. Введите `python main.py`. Если aimbot работает, экспортируйте модель .pt в .engine.

12. Введите `yolo export model="models/sunxds_0.2.1_nano_320.pt" format=engine half=true device=0 workspace=8 imgsz=320`
