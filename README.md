# Google Drive Monitor

Programme qui surveille et redémarre automatiquement Google Drive en cas de problème.

## Construction de l'exécutable

Pour créer un exécutable à partir du fichier `googleDriveMonitor.py`, vous pouvez utiliser PyInstaller. Suivez les étapes ci-dessous pour générer l'exécutable:

1. Installez PyInstaller si ce n'est pas déjà fait:
   ```
   pip install pyinstaller
   ```

2. Utilisez PyInstaller pour créer l'exécutable:
   ```
   pyinstaller --onefile googleDriveMonitor.py
   ```

3. L'exécutable sera généré dans le répertoire `dist`. Vous pouvez le trouver à l'emplacement suivant:
   ```
   dist/googleDriveMonitor.exe
   ```

4. Déplacez l'exécutable à l'emplacement souhaité et exécutez-le avec les options nécessaires.

Note: Assurez-vous que toutes les dépendances nécessaires sont installées dans votre environnement Python avant de créer l'exécutable.


## Utilisation

```
GoogleDriveMonitor.exe [options]
```

### Options disponibles

- `-s` ou `--start-time` : Heure de vérification (format HH:MM)
  - Exemple: `-s "9:30"` pour vérifier à 9h30
  - Défaut: "8:00"

- `-d` ou `--drive-path` : Chemin du lecteur Google Drive
  - Exemple: `-d "S:\GoogleDrive"`
  - Défaut: "S:\GoogleDrive"

- `-a` ou `--app-path` : Chemin de l'exécutable Google Drive
  - Exemple: `-a "C:\Program Files\Google\Drive File Stream\launch.bat"`
  - Défaut: "C:\Program Files\Google\Drive File Stream\launch.bat"

### Exemples

Démarrer avec l'heure par défaut (8:00):
```
GoogleDriveMonitor.exe
```

Définir une heure spécifique:
```
GoogleDriveMonitor.exe -s "9:30"
```

Changer le chemin du lecteur:
```
GoogleDriveMonitor.exe -d "D:\MonDrive"
```

Utiliser plusieurs options:
```
GoogleDriveMonitor.exe -s "7:00" -d "D:\MonDrive" -a "C:\MonChemin\launch.bat"
``` 



