with open ('Desktop/Lista Clasei 11A.txt','r') as f:
    lista=f.readlines()
s,d=0,0
print("     Nume              Prenume           Nota")
for i in lista:
    coloana = i.split()
    s += int(coloana[2])
    d+=1
    print(d,'. ',coloana[0],(16-len(coloana[0]))*' ',coloana[1],(16-len(coloana[1]))*' ',coloana[2])
print("Nota medie a ", d,"elevi este=",s/d)

    
    


