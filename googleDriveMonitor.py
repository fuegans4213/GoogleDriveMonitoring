import os
import time
import datetime
import subprocess
import psutil
import argparse

parser = argparse.ArgumentParser(description='Google Drive Monitor')
parser.add_argument('--drive-path', '-d', default="S:\\GoogleDrive",
                   help='Chemin du lecteur Google Drive')
parser.add_argument('--app-path', '-a',
                   default="C:\\Program Files\\Google\\Drive File Stream\\launch.bat",
                   help='Chemin de l\'exécutable Google Drive')
parser.add_argument('--start-time', '-s', default='8:00',
                    help='Time to check drive access (HH:MM format)')

# Parse arguments once
args = parser.parse_args()

try:
    hour, minute = map(int, args.start_time.split(':'))
except ValueError:
    print("Erreur: Le format de l'heure doit être HH:MM")
    exit(1)

DRIVE_PATH = args.drive_path
APP_PATH = args.app_path

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
    except Exception as e:
        print(f"Error accessing drive: {str(e)}")
        return False


def restart_service():
    subprocess.call(['taskkill', '/IM', 'googledrivefs.exe', '/F'],
                    creationflags=subprocess.CREATE_NO_WINDOW)
    time.sleep(2)
    subprocess.Popen([APP_PATH], creationflags=subprocess.CREATE_NO_WINDOW)


def main():
    while True:

        target_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
        if datetime.datetime.now() > target_time:
            target_time += datetime.timedelta(days=1)

        time.sleep((target_time - datetime.datetime.now()).total_seconds())

        if not check_process() or not check_drive_access():
            restart_service()


if __name__ == "__main__":
    main()
