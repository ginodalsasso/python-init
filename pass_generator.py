import string
import random

def generate_pass():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    pass_length = int(input("Enter the length of the s: \n"))

    s = [] # variable pour stocker le mot de passe
    s.extend(list(s1)) # Ajoute tous les caractères de s1 à s
    s.extend(list(s2))
    s.extend(list(s3)) 
    s.extend(list(s4)) 

    random.shuffle(s) # Mélange les caractères de la liste
    password = ("".join(s[0:pass_length])) # joint les caractères de la liste pour former un mot de passe
    
    print(password)

generate_pass()