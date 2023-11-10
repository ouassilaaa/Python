# Exercice 1 

a= 3
b=12
c= 4
print(a)
print(f"Les trois valeurs de a b et c sont  {a}, {b} et {c}" )
print(f"La somme est des trois variables est  {a+b+c}")

# Exercice 2

max, min=a,a 
if(max<b):
    max=b

if(max<c):
    max=c

if(min>b):
    min=b

if(min>c):
    min=c

print(f"Le min est {min} et le max est {max}")        

# Exercice 4

liste=[]
# userInput=input(f"Ajoutez un nombre à la liste ou appuyer sur q pour quitter")

# if userInput=="q" : 
#     break

while(True):
    n=input("Entrez un nb")
    if n=='q':
        break
    else: 
        if int(n) not in liste:
        liste.append(int(n))

print(liste)        

# Exercice 6

temp_list=[12,14,17,20,15,16,12,25,12,16,25,20,12]
temp_count={}

for temp in temp_list:
    if temp in temp_count:
        temp_count[temp]=+1
    else:
    # temp_count[temp]=1  


# print(f"Température {temp} : {} jours")



