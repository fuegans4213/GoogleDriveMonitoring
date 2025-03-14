import os
import time
import datetime
import subprocess
import psutil

DRIVE_PATH = "S:\\GoogleDrive"  # Remplacer par la lettre du lecteur Google Drive
APP_PATH = "C:\\Program Files\\Google\\Drive File Stream\\launch.bat"  # Chemin de l'exécutable


def check_process():
    try:
        return any(p.name().lower() == 'googledrivefs.exe'
                for p in psutil.process_iter(['name']))
    except psutil.NoSuchProcess:
        return False
    except Exception as e:
        print(f"Erreur psutil : {str(e)}")
        return False

def check_drive_access():
    try:
        test_file = os.path.join(DRIVE_PATH, "drive_test.tmp")
        with open(test_file, 'w') as f:
            f.write(str(datetime.datetime.now()))
        os.remove(test_file)
        return True
    except Exception:
        return False


def restart_service():
    subprocess.call(['taskkill', '/IM', 'googledrivesync.exe', '/F'],
                    creationflags=subprocess.CREATE_NO_WINDOW)
    time.sleep(2)
    subprocess.Popen([APP_PATH], creationflags=subprocess.CREATE_NO_WINDOW)


def main():
    while True:
       # target_time = datetime.datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
       # if datetime.datetime.now() > target_time:
       #    target_time += datetime.timedelta(days=1)

       # time.sleep((target_time - datetime.datetime.now()).total_seconds())

        if not check_process() or not check_drive_access():
            restart_service()


if __name__ == "__main__":
    main()
