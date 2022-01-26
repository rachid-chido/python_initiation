colone = int(input("choisir une colone : "))
ligne  = int(input("choisir une ligne : "))
if(colone == 4 and ligne == 4 ):
     print("touché")
elif (colone == 4 or ligne == 4) : 
     print("En vue.. ")
else:
     print("A l'Eau ")


