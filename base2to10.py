def convertisseur(x):
    binaire=[1]
    a=1
    str_x=str(x)
    for i in range(len(str_x)-1):
        a=a*2
        binaire.append(a)
    binaire.reverse()
    
    nb_decimal=0
    for i in range(len(str_x)):
        if str_x[i]=="1":
            nb_decimal=nb_decimal+binaire[i]
    print("Le nombre binaire ",x ,"vaut ",nb_decimal ,"en base 2. ")
    return nb_decimal

convertisseur(input("Saisissez votre nombre binaire : "))


        
