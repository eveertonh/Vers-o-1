texte = input("Digite alguma coisa: ")

print("tem espaço:> ", texte.isspace())
print("tem números:> ", texte.isnumeric())
print("tem letras:> ", texte.isalpha())
print("tem letrasenumeros:> ", texte.isalnum())