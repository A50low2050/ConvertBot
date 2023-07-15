import os
import shutil
from config import PATH, MEDIA


def clear_media():
    try:
        for address, dirs, files in os.walk(os.path.join(PATH, MEDIA)):
            for name in files:
                os.remove(os.path.join(address, name))

        for dirs in os.listdir(os.path.join(PATH, MEDIA)):
            shutil.rmtree(os.path.join(PATH, MEDIA, dirs))
    except PermissionError as error:
        print(error)
        return '[WinError 32] Процесс не может получить доступ к файлу, так как этот файл занят другим процессом ❗'

    return 'Clear folder is success ✅'

