import webbrowser as wb # Pour ouvrir des URLs
import os # Pour ouvrir des fichiers ou logiciels

def workAuto():
    software_path = "C://Program Files/PathToTheSoftware" # Chemin du logiciel à ouvrir en éxécutant le script
    os.startfile(software_path) # Ouvre le logiciel

    chrome_path = 'C:/Program Files/PathToChrome %s' # Ouvre chrome à l'éxécution du script
    URLS = (
        "google.com", 
        "youtube.com", 
        "github.com"
        )
    
    for url in URLS:
        wb.get(chrome_path).open(url) # Ouvre les URLs dans Chrome
    
workAuto()