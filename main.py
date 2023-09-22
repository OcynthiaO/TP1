chaine = str(input('Entrer une chaine de caracteres:'))
def count_word(str):
    nombre = len(chaine.split(" "))
    return nombre

print("nombre de mot : " + '' + str(count_word(chaine)))