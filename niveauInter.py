# username= "Zelda"
# weather= "les températures aujourd'hui ne dépassera pas les 14 degrès"
# userList=["Zelda", "Alexis", "Romain", "Ouassila"]

# # if username=="Pierre": 
# #     print(f"Bienvenue {username},")
# #     print("Météo du jour:", weather)

# # else: print("Welcome stranger :) ")

# if (username in userList): 
#     print(f"Bienvenue {username},")
#     print("Météo du jour:", weather)

# else: print("Welcome stranger :) ")

# price= 20

# if(price > 10 ): 
#     print ("C'est cher")
    
# else: print("Bon prix")

# # Modulo d'un nb 

# nb=int(input("Entrez un nombre: "))
# # print("Le reste de la division euclidienne de  :", nb,"est : ", nb%2)

# # Nb pair ou impair

# if(nb%2)==0:
#     print(f"Le nombre {nb} est pair")

# else: 
#     print(f"Le nombre {nb} est impair")

# Calculer la racine carré d'un nb dans une liste    

# maListe=[0,1,2,10,56,3,9,8]

# for i in maListe: 
#     print(i, i*i)

# Fonction range : permet d'aller plus vite, ici pas besoin d'inclure tous les entiers on lui donne directement la fourchette voulue 

# Cas 1 : on utilise range pour qu'il calcul les nombres jusqu'a 10 non inclus: parametre 1 nb
for i in range(10):
    print(i, i*i)

# Cas 2: on utilise range en lui donnant un nb de départ et d'arrriver
for j in range(3,20):
    print(j,j-2)

#Cas 3: on peut ajouter une troisième valeur qui sera  le paramètre pour incrémenter si on ne veut pas que ca soit 1
for k in range(2,25,2):
    print (k,k*2)

# Boucle while : contrairement a for nécessite de définir i en l'initialisant

i=0
while i < 10 :
    print("Dans la boucle", i)
    i += 1

print("La condition n'est plus respectée")


# Les listes: possible de mixer différent genre de valeur dans un même tableau, mais déconseillé car pb pour les calculs

