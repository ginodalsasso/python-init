import string 
import random
from csv import writer # pour écrire dans un fichier csv

def generate_pass():
    s1 = string.ascii_lowercase # Crée une liste de caractères minuscules
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    platform = input("Enter the platform: \n") # Demande à l'utilisateur de saisir la plateforme où le mot de passe sera utilisé
    pass_length = int(input("Enter the length of the password: \n"))

    s = [] # variable pour stocker le mot de passe
    s.extend(list(s1)) # Ajoute tous les caractères de s1 à s
    s.extend(list(s2))
    s.extend(list(s3)) 
    s.extend(list(s4)) 

    random.shuffle(s) # Mélange les caractères de la liste
    password = ("".join(s[0:pass_length])) # joint les caractères de la liste pour former un mot de passe
    
    print(password)

    passdata = [platform, password] # Stocke la plateforme et le mot de passe dans une liste
    with open('pass.csv', 'a') as f: # Crée un fichier csv
        writedata = writer(f) # Écrit dans le fichier csv
        writedata.writerow(passdata) # Écrit les données dans le fichier csv

generate_pass()