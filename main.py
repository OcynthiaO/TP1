

chaine = str(input('Entrer une chaine de mots:'))
def count_word(str):
    nombre = len(chaine.split(" "))
    return nombre

print("nombre de mot : " + '' + str(count_word(chaine)))