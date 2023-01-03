# PARTIE 1

#______________Exo 1

print ("Exo 1")
print (".")

myTable = [12,52,16,20,35]      #Création d'un tableau (qui sera le meme pour tout le devoir)
print(myTable)                  # Montrer le tableau 

numeroRetenue = myTable[2]      # On retien l'élément de l'indice 2 (donc le 3ème, étant donnée que l'on compte à partir de 0) 
myTable[2] = myTable[1]         # L'indice 2 prend la valeur de l'indice 1
myTable[1] = numeroRetenue      # L'indice 1 prend la valeur de l'élément retenue auparavant

print (myTable)                 # Montrer le nouveau tableau

#______________Exo 2

print (".")
print ("Exo 2")
print (".")

myTable = [12,52,16,20,35]
print(myTable)                      # Montrer le tableau 


valMin = 100

plusGrand = myTable[0]              # On créer un élément qui prend la valeur de celui de l'indice 0 du tableau
for i in range(0,len(myTable)):
    if(myTable[i] > plusGrand):     # Pour quelconque indice "i" dont la valeur est superieur au plus grand nombre
        plusGrand = myTable[i]      # le plus grand nombre prend la valeur de "i"
        
print(plusGrand)                    # Montrer qui est le plus grand

numeroRetenue = myTable[i]          # On retien la valeur de l'indice "i"
myTable[i] = myTable[1]             # L'indice "i" prend la valeure de l'indice 1
myTable[1] = numeroRetenue          # et la valeur de l'indice 1 prend la valeur retenu auparavant

print (myTable)                     # Montrer le nouveau tableau



#______________Exo 3

print (".")
print ("Exo 3")
print (".")



myTable = [12,52,16,20,35]          

print(myTable)                                          # Montrer le nouveau tableau

for j in range(len(myTable)):                       
    valMin=100                                          #Création d'une valeur
    for i in range(j,len(myTable)):                      
        if(myTable[i]<valMin):                          # pour toute valeur "i" inferieur à la "valMin"
            valMin = myTable[i]                         # la retenue prend la valeur de celle de l'indice "i"
            indiceMin = i                               # "indiceMin" prend comme valeur le numéro "i" (pas son contenue, mais lui-même)
    numeroRetenue = myTable[j]                          # le "numéroRetenue" prend la valeur de l'indice "j"
    myTable[j] = myTable[indiceMin]                     # la valeur de l'indice "j" prend la valeur de l'"indiceMin" 
    myTable[indiceMin] = numeroRetenue                  # la valeur de l'"indiceMin" prend la valeur de la retenue

print(myTable)

#______________Exo 4

print (".")
print ("Exo 4")
print (".")

print("Le tri à bulles est considéré comme lent car il doit ")
print("analyser tout le tableau, élément par élément")
print("puis ensuite intervertir tous ceux-ci un par un également.")
print("")




