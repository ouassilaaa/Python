print("Hello world!")

nom= input ("Quel est votre nom ?")
prenom= input ('Quel est votre prénom ?')

nomComplet=nom +" "+ prenom

print (f'Bonjour {nomComplet} bienvenue ! ')

# Afficher longueur de la chaine
print(len(nomComplet))

age=15
print(age)

print("Joyeux anniversaire", age +1, "ans aujourd'hui! ")

# Passer de degré en radian

angleDeg= 10
angleRad= (angleDeg * 3.14)/180
print(angleRad) 

# Pour concaténer un string avec int il faudra convertir int en str
nomCompletAge = nom + " " + prenom + " " + str(age)
print(nomCompletAge)

prenom= "Tom"
nom="Cruz"
age=59
print ("Bonjour je m'appelle", prenom, "jai", str(age), "ans" )

# Formatage f-string : pas besoin de convertir les int en string ici ca se fait auto, attention tout se converti en string il faut donc repasser en int si besoin de faire des calculs avec les données
print(f"Bonjour je m'appelle {prenom} j'ai {age} ans")

prenom2=input ("Quelle est votre prénom ? ")
nom2=input ("Quelle est votre nom ? ")
age2=input("Quelle est votre âge ? ")

print (f"Affiche: Bienvenue {prenom2} {nom2} vous avez {age2} ans aujourd'hui! ")

# Calculatrice
# On passe en float car on ne peut pas faire d'opération mathématique avec les str,  il faudra absolument convertir
nombre1= float(input("Entrez un premier nombre "))
nombre2= float(input("Entrez un deuxième nombre "))

print("Addition des deux nombres =  ", nombre1 + nombre2)
print("Soustraction des deux nombres =  ", nombre1 - nombre2)
print("Division des deux nombres =  ", nombre1/nombre2)






