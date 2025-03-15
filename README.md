# Google Drive Monitor

Programme qui surveille et redémarre automatiquement Google Drive en cas de problème.

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